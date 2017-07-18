#include "widget.h"


// AI核心

void Widget::statisticwinWays() {

    winsWayCount = 0;

    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 15; ++j) {
            for (int k = 0; k < 600; ++k) {
                winsArr[i][j][k] = false;
            }
        }
    }

    //  横向数组

    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 11; ++j) {
            for (int k = 0; k < 5; ++k) {
                winsArr[i][j + k][winsWayCount] = true;
            }
            winsWayCount++;
        }
    }

    //  纵向
    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 11; ++j) {
            for (int k = 0; k < 5; ++k) {
                winsArr[j + k][i][winsWayCount] = true;
            }
            winsWayCount++;
        }
    }

    //  主对角线方向
    for (int i = 0; i < 11; ++i) {
        for (int j = 0; j < 11; ++j) {
            for (int k = 0; k < 5; ++k) {
                winsArr[i + k][j + k][winsWayCount] = true;
            }
            winsWayCount++;
        }
    }


    // 副对角线方向
    for (int i = 0; i < 11; ++i) {
        for (int j = 14; j > 3; --j) {
            for (int k = 0; k < 5; ++k) {
                winsArr[i + k][j - k][winsWayCount] = true;
            }
            winsWayCount++;
        }
    }

    qDebug() << "Win Ways number is " << winsWayCount << endl;

}


void Widget::initScore() {
    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 15; ++j) {
            playerScore[15][15] = 0;
            computerScore[15][15] = 0;
        }
    }
}

int Widget::getScore() {

    int w = 0;

    int winNumCase[2][4];
    // winNumCase[0] player
    // winNumCase[1] AI
    for (int j = 0; j < 2; ++j) {
        for (int i = 0; i < 4; ++i) {
            winNumCase[j][i] = 0;
        }
    }

    initScore();

    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 15; ++j) {
            if (playMap[i][j] != 0) continue;
            for (int k = 0; k < winsWayCount; ++k) {
                if (winsArr[i][j][k]) {
                    switch (playerWinsWayStatisticArr[k]) {
                        case 1:
                            playerScore[i][j] += 5;
                            winNumCase[0][0]++;
                            break;
                        case 2:
                            playerScore[i][j] += 50;
                            winNumCase[0][1]++;
                            break;
                        case 3:
                            if (!live3(i, j, "p")) {
                                playerScore[i][j] += 100;
                                winNumCase[0][2]++;
                            } else {
                                winNumCase[0][3]++;
                                playerScore[i][j] += 1000;
                            }
                                break;
                        case 4:
                            playerScore[i][j] += 1000;
                            winNumCase[0][3]++;
                            break;
                    }
                    switch (computerWinsWayStatisticArr[k]) {
                        case 1:
                            computerScore[i][j] += 5;
                            winNumCase[1][0]++;
                            break;
                        case 2:
                            computerScore[i][j] += 50;
                            winNumCase[1][1]++;
                            break;
                        case 3:
                        if (!live3(i, j, "c")) {
                            computerScore[i][j] += 100;
                            winNumCase[1][2]++;
                        } else {
                            computerScore[i][j] += 1000;
                            winNumCase[1][3]++;
                        }
                            break;

                        case 4:
                            computerScore[i][j] +=  1000;
                            winNumCase[1][3]++;
                            break;
                    }
                }
            }
        }
    }


    int wMax = winNumCase[0][0]*5 + winNumCase[0][1]*50 + winNumCase[0][2]*100 + winNumCase[0][3]*1000;

    int wMin = winNumCase[1][0]*5 + winNumCase[1][1]*50 + winNumCase[1][2]*100 + winNumCase[1][3]*1000;

    return wMax-wMin;
}

void Widget::getAvaliablePos() {
    avaliableStep.clear();
    int i,j,k;
    for (i = 0; i < 15; ++i) {
        for (j = 0; j < 15; ++j) {
            if (playMap[i][j] != 0) continue;
            if (playerScore[i][j] > 0 || computerScore[i][j] >= 2) {
                avaliableStep.insert(std::pair<int, QPoint>(std::max(playerScore[i][j], computerScore[i][j]), QPoint(i,j)));
            }
        }
    }
}




bool Widget::__live3__(int r, int c, int t) {
    int i, j;
    // 1.2.#*000*#
    //3 4 00*0#####
    // 5.0 0*0 0

    //1 *000
    // 行
    int count = 0;
    for (i = c + 1; i <= c+3 && i<15 && playMap[r][i] == t; ++i) {
        count++;
    }
    if (count == 3 && i<15 && playMap[r][i] == 0) {
//        qDebug() << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$1 row\n";
        return true;
    }
    // 列
    count = 0;
    for (i = r + 1; i <= r+3 && i <15 && playMap[i][c] == t; ++i) {
        count++;
    }
    if (count == 3 && i<15 && playMap[i][c] == 0) {
//        qDebug() << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$2 row\n";
        return true;
    }
    // 主对角线
    count = 0;
    for(i = r + 1, j = c + 1; i <= r+3 && i<15 && j <= c+3 && j<15 && playMap[i][j] == t; ++j, ++i) {
        count++;
    }
    if (count == 3 && i<15 && j<15 && playMap[i][j] == 0) {
        return true;
    }
    //福对角线
    count = 0;
    for(i = r + 1, j = c - 1; i <= r+3 && i < 15 && j >= c-3 && j>=0 && playMap[i][j] == t; --j, ++i) {
        count++;
    }
    if (count == 3 && i < 15 && j>= 0 && playMap[i][j] == 0) {
        return true;
    }
    // 2 000*
    // 行
    count = 0;
    for (i = c - 1; i >= c-3 && i>=0 && playMap[r][i] == t; --i) {
        count++;
    }
    if (count == 3 && i>=0 && playMap[r][i] == 0) {
        return true;
    }
    // 列
    count = 0;
    for (i = r - 1; i >= r-3 && i >=0 && playMap[i][c] == t; --i) {
        count++;
    }
    if (count == 3 && i>=0 && playMap[i][c] == 0) {
        return true;
    }
    // 主对角线
    count = 0;
    for(i = r - 1, j = c - 1; i >= r-3 && i>=0 && j >= c-3 && j>=0 && playMap[i][j] == t; --j, --i) {
        count++;
    }
    if (count == 3 && i>=0 && j>=0 && playMap[i][j] == 0) {
        return true;
    }
    //福对角线
    count = 0;
    for(i = r - 1, j = c + 1; i >= r-3 && i>=0 && j <= c+3 && j<15 && playMap[i][j] == t; ++j, --i) {
        count++;
    }
    if (count == 3 && i>=0 && j<15 && playMap[i][j] == 0) {
        return true;
    }
    //3 00*0#####
    // 行
    count = 0;
    for (i = c - 1; i >= c-2 && i>=0 && playMap[r][i] == t; --i) {
        count++;
    }
    if (c + 1 < 15 && playMap[r][c+1] == t) {
        count++;
    }
    if (count == 3 && i>=0 && playMap[r][i] == 0 && c+2 < 15 && playMap[r][c+2] == 0) {
        return true;
    }
    // 列
    count = 0;
    for (i = r - 1; i >= r-2 && i >=0 && playMap[i][c] == t; --i) {
        count++;
    }
    if (r + 1 < 15 && playMap[r+1][c] == t) {
        count++;
    }
    if (count == 3 && i>=0 && playMap[i][c] == 0 && r+2 < 15 && playMap[r+2][c] == 0) {
        return true;
    }
    // 主对角线
    count = 0;
    for(i = r - 1, j = c - 1; i >= r-2 && i>=0 && j >= c-2 && j>=0 && playMap[i][j] == t; --j, --i) {
        count++;
    }
    if (r + 1 < 15 && c + 1 < 15 && playMap[r+1][c+1] == t) {
        count++;
    }
    if (count == 3 && i>=0 && j>=0 && playMap[i][j] == 0 && r+2<15 && c+2<15 && playMap[r+2][c+2] == 0) {
        return true;
    }
    //福对角线
    count = 0;
    for(i = r - 1, j = c + 1; i >= r-2 && i>=0 && j <= c+2 && j<15 && playMap[i][j] == t; ++j, --i) {
        count++;
    }
    if (r + 1 < 15 && c - 1 >= 0 && playMap[r+1][c+1] == t) {
        count++;
    }
    if (count == 3 && i>=0 && j<15 && playMap[i][j] == 0 && r + 2 < 15 && c - 2 >= 0 && playMap[r+2][c-2] == 0) {
        return true;
    }

    //4 0*00#####
    // 行
    count = 0;
    for (i = c+1; i <= c+2 && i < 15 && playMap[r][i] == t; ++i) {
        count++;
    }
    if (c - 1 >= 0 && playMap[r][c-1] == t) {
        count++;
    }
    if (count == 3 && i<15 && playMap[r][i] == 0 && c-2 >= 0 && playMap[r][c-2] == 0) {
        return true;
    }
    // 列
    count = 0;
    for (i = r + 1; i <= r+2 && i<15 && playMap[i][c] == t; ++i) {
        count++;
    }
    if (r - 1 >= 0 && playMap[r-1][c] == t) {
        count++;
    }
    if (count == 3 && i<15 && playMap[i][c] == 0 && r - 2 >= 0 && playMap[r-2][c] == 0) {
        return true;
    }
    // 主对角线
    count = 0;
    for(i = r + 1, j = c + 1; i <= r+2 && i<15 && j <= c+2 && j<15 && playMap[i][j] == t; ++j, ++i) {
        count++;
    }

    if (r - 1 >= 0 && c - 1 >= 0 && playMap[r-1][c-1] == t) {
        count++;
    }
    if (count == 3 && i<15 && j<15 && playMap[i][j] == 0 && r-2>=0 && c-2>=0 && playMap[r-2][c-2] == 0) {
        return true;
    }
    //福对角线
    count = 0;
    for(i = r + 1, j = c - 1; i <= r+2 && i<15 && j >= c-2 && j>=0 && playMap[i][j] == t; ++j, --i) {
        count++;
    }
    if (r - 1 >= 0 && c + 1 < 15 && playMap[r-1][c+1] == t) {
        count++;
    }
    if (count == 3 && i<15 && j>=0 && playMap[i][j] == 0 && r - 2 >= 0 && c + 2 < 15 && playMap[r-2][c+2] == 0) {
        return true;
    }
    return false;
    // 5 0 0*0 0


}

bool Widget::live3(int r, int c, QString who) {
    if (who == "c") {
        if (firstPlay) {
            return __live3__(r,c,2);
        } else {
            return __live3__(r,c,1);
        }
    } else {
        if (firstPlay) {
            return __live3__(r,c,1);
        } else {
            return __live3__(r,c,2);
        }
    }
}

void Widget::getMaxScore() {
    int tx = 0;
    int ty = 0;
    int tMax = 0;
    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 15; ++j) {
            if (playMap[i][j] == 0 && tMax < playerScore[i][j]) {
                tx = i;
                ty = j;
                tMax = playerScore[i][j];
            }
        }
    }
    player_max.setX(tx);
    player_max.setY(ty);


    tx = ty = 0;
    tMax = 0;
    for (int i = 0; i < 15; ++i) {
        for (int j = 0; j < 15; ++j) {
            if (playMap[i][j] == 0 && tMax < computerScore[i][j]) {
                tx = i;
                ty = j;
                tMax = computerScore[i][j];
            }
        }
    }
    AI_max.setX(tx);
    AI_max.setY(ty);
}




void Widget::rollback(int r, int c, char who) {
    static int ki = 0;
    ki++;
    qDebug() << "##################" << endl;
    qDebug() << "Roll Back" << " " << ki << endl;
    qDebug() << "##################" << endl;

    playMap[r][c]=0;

    for (int i = 0; i < winsWayCount; ++i) {
        if (winsArr[r][c][i]) {
            if (who == 'p') {
                playerWinsWayStatisticArr[i]--;
                computerWinsWayStatisticArr[i]++;
            } else {
                playerWinsWayStatisticArr[i]++;
                computerWinsWayStatisticArr[i]--;
            }
        }
    }

    if (turns == 1) {
        turns = 2;
    } else {
        turns = 1;
    }
}

void Widget::set_a_chess(int r, int c, char who) {
    static int kj = 0;
    kj++;
    qDebug() << "##################" << endl;
    qDebug() << "Set A Chess" << " "<< kj << endl;
    qDebug() << "##################" << endl;

//    if (who == 'p') {
//        if (firstPlay) {
//            playMap[r][c] = 1;
//        } else {
//            playMap[r][c] = 2;
//        }
//    } else {
//        if (firstPlay) {
//            playMap[r][c] = 2;
//        } else {
//            playMap[r][c] = 1;
//        }
//    }

    for (int i = 0; i < winsWayCount; ++i) {
        if (winsArr[r][c][i]) {
            if (who == 'p') {
                playerWinsWayStatisticArr[i]++;
                computerWinsWayStatisticArr[i]--;
            } else {
                playerWinsWayStatisticArr[i]--;
                computerWinsWayStatisticArr[i]++;
            }
        }
    }


    playMap[r][c] = turns;
    if (turns == 1) {
        turns = 2;
    } else {
        turns = 1;
    }
}


void Widget::getAI_next()
{
    thinkDeep = 1;

    initScore();

    getScore();


    deep_min(thinkDeep, -INF, false);

    qDebug() << "##################" << endl;
    qDebug() << "AI next " << AI_max.x() << " " << AI_max.y() << endl;
    qDebug() << "##################" << endl;


    countChess++;
    currentPoint.setX(AI_max.x());
    currentPoint.setY(AI_max.y());
    playMap[AI_max.x()][AI_max.y()] = turns;
    chessLise.push_back(currentPoint);

    changeTurn();


    qDebug() << "***********************";
    qDebug() << "Latest update";
    qDebug() << "***********************";


    this->update();


    for (int i = 0; i < winsWayCount; ++i) {
        // 靠近胜利+1
        if (winsArr[AI_max.x()][AI_max.y()][i]) {
            computerWinsWayStatisticArr[i]++;
            // i方法下人类无法赢
            playerWinsWayStatisticArr[i] = 10;
            if (computerWinsWayStatisticArr[i] == 5) {
                winShow();
                break;
            }
        }
    }

    if (gameStart && countChess == 15 * 15) {
        tie();
    }

    qDebug() << "@@@@@@@@@@@@@@@@@@@@@@@@";
    qDebug() << "AI end on turn";
    qDebug() << "@@@@@@@@@@@@@@@@@@@@@@@@";



}
int Widget::deep_max(int deep, int parentBeta, bool con) {


    if (deep == 0) {
        return getScore();
    }


    int alpha = -INF;
    int beta = parentBeta;

    QPoint bestPos;

    int tempW;

    getAvaliablePos();

    qDebug() << "^^^^^^^^^^^^^^^^^^^^^^^^";
    qDebug() << "In Max" << deep << " " << avaliableStep.size();
    qDebug() << "^^^^^^^^^^^^^^^^^^^^^^^^^";


    bool hasWin = false;


    for (auto it = avaliableStep.begin(); it != avaliableStep.end(); ++it) {
        // %%
        set_a_chess((it->second).x(), (it->second).y(), 'p');




        if (!hasWin) tempW = deep_min(deep - 1, alpha, hasWin);



        // %%
        rollback((it->second).x(), (it->second).y(), 'p');


        if (hasWin) {
            bestPos.setX((it->second).x());
            bestPos.setY((it->second).y());
            alpha = INF;
            break;
        }

        if (alpha <= tempW) {
            bestPos.setX((it->second).x());
            bestPos.setY((it->second).y());
            alpha = tempW;
        }



        if (alpha >= beta) {
            break;
        }
    }
//    bestChoic ans;
    AI_max = bestPos;
//    ans.weight = alpha;

    return alpha;

}

int Widget::deep_min(int deep, int parentAlpha, bool con) {

    int alpha = parentAlpha;

    QPoint bestPos;


    int beta = INF;


    if (deep == 0) {
        return getScore();
    }



    int tempW;

    getAvaliablePos();

    qDebug() << "^^^^^^^^^^^^^^^^^^^^^^^^";
    qDebug() << "In Min" << deep << " " << avaliableStep.size();
    qDebug() << "^^^^^^^^^^^^^^^^^^^^^^^^^";

    bool hasWin = false;

    for (auto it = avaliableStep.begin(); it != avaliableStep.end(); ++it) {

        // %%
        set_a_chess( (it->second).x(), (it->second).y(), 'c');




        if (!hasWin) tempW = deep_max(deep - 1, beta, hasWin);




        // %%
        rollback((it->second).x(), (it->second).y(), 'c');

        if (hasWin) {
            bestPos.setX((it->second).x());
            bestPos.setY((it->second).y());
            beta = -INF;
            break;
        }

        if (beta >= tempW) {
            bestPos.setX((it->second).x());
            bestPos.setY((it->second).y());
            beta = tempW;
        }




        if (alpha >= beta) {
            break;
        }
    }

    AI_max = bestPos;


    return beta;

}


