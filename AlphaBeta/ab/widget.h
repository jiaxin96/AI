#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QFont>
#include <QMouseEvent>
#include <QPainter>
#include <QDebug>
#include <QRect>
#include <QPen>
#include <QPalette>
#include <QList>
#include <QPoint>
#include <QMessageBox>
#include <stdlib.h>
#include <unistd.h>
#include <map>
using namespace std;
#define INF 999999
namespace Ui {
class Widget;

}



class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

    struct bestChoice {
        QPoint pos;
        int weight;
        bestChoice(QPoint p =  QPoint(0,0), int w = 0) {
            pos = p;
            weight = w;
        }
    };


public slots:
    void startFirstButClicked();
    void startLaterButClicked();
    void exitButClicked();
    void backOneButClicked();

private:

    // UI布局 按钮界面设计
    Ui::Widget *ui;
    QLabel *whichOneTurn;
    QLabel *whichOneTurnMess;
    QPushButton *startFirstBut;
    QPushButton *startLaterBut;
    QPushButton *exitBut;
    QPushButton *backOne;




//    QPushButton *playOrder;




    // 棋类数组
    int playMap[15][15];


    // 游戏开局 结束逻辑判断
    // 是否先手
    bool firstPlay;
    int turns;
    bool checkWin();
    void winShow();
    void changeTurn();
    void tie();
    void init();
    bool gameStart;
    bool canStart;
    int countChess;


    // 悔棋
    QList<QPoint> chessLise;

    // AI 部分
    // #####
    // #####

    // 从1开始计数
    // 实际赢法数组从0开始计数

    // 通过statisticWinWays计算得到
    int winsWayCount;

    QPoint AInext;
    QPoint AI_max;
    QPoint player_max;

    QPoint currentPoint;

    // AI核心
    void getAI_next();
    void statisticwinWays();
    int getScore();
    void initScore();
    void getMaxScore();

    void set_a_chess(int r, int c, char who);

    void rollback(int r, int c, char who);

    // 统计数组
    int playerWinsWayStatisticArr[600];
    int computerWinsWayStatisticArr[600];

    // 评分数组
    int playerScore[15][15];
    int computerScore[15][15];


    // 赢法数组
    bool winsArr[15][15][600];


    //  加强思考



    multimap<int, QPoint> avaliableStep;

    bool live3(int r, int c, QString who);
    bool __live3__(int r, int c, int t);

    int thinkDeep = 3;

    int deep_min(int i, int p, bool con);
    int deep_max(int i, int p, bool con);


    void getAvaliablePos();


    //bestChoic td();

    int deep_evalue();


    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event);
    void paintEvent(QPaintEvent *event);
};


#endif // WIDGET_H
