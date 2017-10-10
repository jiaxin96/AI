import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.LinkedList;

/**
 * Created by jx on 7/5/17.
 */
public class PlayBoardPanel extends JPanel {

    private Image whiteImg, blackImg, boardImg, currentImg;
    public static final int board_w = 600;
    public static final int board_h = 600;
    public static  final  int chess_w = 30, chess_h = 30;
    public static  final  int board_origin_x = 30, board_origin_y = 30;
    public static final int rowCount = 19, columnCount = 19;
    public static final int statesCount = 2;

    public static boolean start_game = false;
    public  static  boolean firstPlay = true;


    // 0 for nothing
    // 1 for black
    // 2 for white
    private int[][] board = new int[rowCount][columnCount];
    private char[] states = new char[]{'b','w'};
    private int nextState = 0;

    private int chessCount = 0;
    private LinkedList<ChessInfo> allChess = new LinkedList<ChessInfo>();
    private ChessInfo currentChess = new ChessInfo(9,9,'w');

//AI START

    private ChessInfo bestChose = new ChessInfo();

    private int winsWayCount = 0;
    private int[] blackWinsWayStatisticArr = new int[1200];
    private int[] whiteWinsWayStatisticArr = new int[1200];
    private boolean[][][] winsArr = new boolean[19][19][1200];

    private boolean blackWin = false;
    private boolean whiteWin = false;

    private final int INF = 99999;


//AI END
    //统计赢法 1020种
    private void statisticWinWays() {
        winsWayCount = 0;

        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < columnCount; ++j) {
                for (int k = 0; k < 1200; ++k) {
                    winsArr[i][j][k] = false;
                }
            }
        }

        //  横向数组

        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < columnCount-4; ++j) {
                for (int k = 0; k < 5; ++k) {
                    winsArr[i][j + k][winsWayCount] = true;
                }
                winsWayCount++;
            }
        }

        //  纵向
        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < columnCount -4; ++j) {
                for (int k = 0; k < 5; ++k) {
                    winsArr[j + k][i][winsWayCount] = true;
                }
                winsWayCount++;
            }
        }

        //  主对角线方向
        for (int i = 0; i < rowCount - 4; ++i) {
            for (int j = 0; j < columnCount - 4; ++j) {
                for (int k = 0; k < 5; ++k) {
                    winsArr[i + k][j + k][winsWayCount] = true;
                }
                winsWayCount++;
            }
        }


        // 副对角线方向
        for (int i = 0; i < rowCount - 4; ++i) {
            for (int j = columnCount - 1; j > 3; --j) {
                for (int k = 0; k < 5; ++k) {
                    winsArr[i + k][j - k][winsWayCount] = true;
                }
                winsWayCount++;
            }
        }

        System.out.println("Debug:" + "the number of win ways is " + winsWayCount + "!!!");
    }

    //min-max-search start
    // black : max
    // white : min
    private void MinMaxSearch() {
        if (firstPlay) {
            maxSearch(5, INF);
        } else {
            minSearch(5,-INF);
        }
        PutChess((int) bestChose.getX(), (int) bestChose.getY());
        repaint();
    }

    private int minSearch(int depth, int alpha) {
        int r = 0,c = 0,beta = INF;
        if (depth == 0) {
            beta = evaluate();
            return beta;
        } else {
            LinkedList<ChessInfo> availableSteps = getAvailableSteps('w');
            for (ChessInfo step : availableSteps) {
                PutChess((int) step.getX(), (int) step.getY());
                if (checkWin('w') == true) {
                    beta = -INF;
                    r = (int) step.getX();
                    c = (int) step.getY();
                    rollBackAStep();
                    break;
                } else {
                    int temp = maxSearch(depth-1, beta);
                    rollBackAStep();
                    if (temp < beta) {
                        beta = temp;
                        r = (int) step.getX();
                        c = (int) step.getY();
                    }
                    if (alpha >= beta) {
                        break;
                    }
                }
            }
            setBestChose(r, c);
            return beta;
        }
    }

    private int maxSearch(int depth, int beta) {
        int r = 0,c = 0,alpha = -INF;
        if (depth == 0) {
            alpha = evaluate();
            return alpha;
        } else {
            LinkedList<ChessInfo> availableSteps = getAvailableSteps('b');
            for (ChessInfo step : availableSteps) {
                PutChess((int) step.getX(), (int) step.getY());
                if (checkWin('b') == true) {
                    alpha = INF;
                    r = (int) step.getX();
                    c = (int) step.getY();
                    rollBackAStep();
                    break;
                } else {
                    int temp = minSearch(depth-1, alpha);
                    rollBackAStep();
                    if (temp > alpha) {
                        alpha = temp;
                        r = (int) step.getX();
                        c = (int) step.getY();
                    }
                    if (alpha >= beta) {
                        break;
                    }
                }
            }
            setBestChose(r, c);
            return alpha;
        }
    }

    private void setBestChose(int r,int c) {
        bestChose.setLocation(r,c,states[nextState]);
    }

    private boolean checkWin(char type) {
        if (type == 'b') {
            return  blackWin;
        }
        return  whiteWin;
    }

    private LinkedList<ChessInfo> getAvailableSteps(char type) {
        LinkedList<ChessInfo> ans5 = new LinkedList<>();
        LinkedList<ChessInfo> ans4 = new LinkedList<>();
        LinkedList<ChessInfo> ans3 = new LinkedList<>();
        LinkedList<ChessInfo> ans2 = new LinkedList<>();
        LinkedList<ChessInfo> ans1 = new LinkedList<>();
        LinkedList<ChessInfo> ans0 = new LinkedList<>();

        for (int i = 0; i < rowCount; ++i) {
            for (int j = 0; j < columnCount; ++j) {
                for (int k = 0; k < winsWayCount; ++k) {
                    if (winsArr[i][j][k] == true && board[i][j] == 0) {
                        if (type == 'w') {
                            switch (whiteWinsWayStatisticArr[k]) {
                                case 1:
                                    if (ans1.size() <= 15) {
                                        ans1.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 2:
                                    if (ans2.size() <= 12) {
                                        ans2.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 3:
                                    if (ans3.size() <= 10) {
                                        ans3.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 4:
                                    if (ans4.size() <= 8) {
                                        ans4.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 5:
                                    if (ans5.size() <= 3) {
                                        ans5.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                            }
                        } else {
                            switch (blackWinsWayStatisticArr[k]) {
                                case 1:
                                    if (ans1.size() <= 15) {
                                        ans1.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 2:
                                    if (ans2.size() <= 12) {
                                        ans2.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 3:
                                    if (ans3.size() <= 10) {
                                        ans3.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 4:
                                    if (ans4.size() <= 8) {
                                        ans4.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                                case 5:
                                    if (ans5.size() <= 3) {
                                        ans5.addLast(new ChessInfo(i,j));
                                    }
                                    break;
                            }
                        }
                    }
                }
            }
        }

        if (ans5.size() > 0) {
            return ans5;
        } else if (ans4.size() > 0) {
            return  ans4;
        } else if (ans3.size() > 0) {
            return ans3;
        } else if (ans2.size() > 0) {
            return ans2;
        } else if (ans1.size() > 0) {
            return ans1;
        } else {
            if (board[9][9] == 0) {
                ans0.add(new ChessInfo(9,9));
            }
            return ans0;
        }
    }
    // min-max-search end

    // evaluate start
    // black_value - white_value
    private int evaluate() {
        int fiveV = 5000, fourV = 1500, triV = 800, twoV = 500, oneV = 100;
        int blackV = 0, whiteV = 0;
        for (int i = 0; i < winsWayCount; ++i) {
            switch (blackWinsWayStatisticArr[i]) {
                case 1:
                    blackV += oneV;
                    break;
                case 2:
                    blackV += twoV;
                    break;
                case 3:
                    blackV += triV;
                    break;
                case 4:
                    blackV += fourV;
                    break;
                case 5:
                    blackV += fiveV;
                    break;
            }


            switch (whiteWinsWayStatisticArr[i]) {
                case 1:
                    whiteV += oneV;
                    break;
                case 2:
                    whiteV += twoV;
                    break;
                case 3:
                    whiteV += triV;
                    break;
                case 4:
                    whiteV += fourV;
                    break;
                case 5:
                    whiteV += fiveV;
                    break;
            }
        }

        return blackV-whiteV;
    }
    // evaluate end

    public PlayBoardPanel() {
        Toolkit tk = Toolkit.getDefaultToolkit();
        whiteImg =  tk.getImage("/home/jx/Desktop/codes/AI/五子棋/FiveAiJava/res/white.jpg");
        blackImg = tk.getImage("/home/jx/Desktop/codes/AI/五子棋/FiveAiJava/res/black.jpg");
        boardImg = tk.getImage("/home/jx/Desktop/codes/AI/五子棋/FiveAiJava/res/board.jpg");
        currentImg = tk.getImage("/home/jx/Desktop/codes/AI/五子棋/FiveAiJava/res/focus.png");

        MediaTracker tracker = new MediaTracker(this);
        tracker.addImage(boardImg,1);
        tracker.addImage(whiteImg,2);
        tracker.addImage(blackImg,3);
        tracker.addImage(currentImg,4);

        try {
//            tracker.waitForID(1);
//            tracker.waitForID(2);
//            tracker.waitForID(3);
//            tracker.waitForID(4);
            tracker.waitForAll();
        } catch (Exception e) {
            System.out.println(e.getStackTrace());
        }

        statisticWinWays();

        this.addMouseListener(new PutAChessListener());
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Color c = g.getColor();
        g.setColor(Color.black);
        System.out.println("Debug:Paint!!!!!!!!");
        g.drawImage(boardImg, 0, 0,this.getWidth(), this.getHeight(), this);
//        g.drawImage(blackImg, 45,45,30,30,this);

        for (int i = 0 ; i < rowCount; i++) {
            for (int j = 0; j < columnCount; ++j) {
                int y = board_origin_y + i*chess_h - chess_h/2;
                int x = board_origin_x + j*chess_w - chess_w/2;
                switch (board[i][j]) {
                    case 0:
                        break;
                    case 1:
                        g.drawImage(blackImg, x,y,chess_w,chess_h,this);
                        break;
                    case 2:
                        g.drawImage(whiteImg, x,y,chess_w,chess_h,this);
                        break;
                    default:
                        break;
                }
            }
        }

        // currentChess
        if (currentChess.getState() != 'n') {
            System.out.println("Debug:current!!!!!!!!!");
            int y = board_origin_y + (int) currentChess.getX()*chess_h - chess_h/2;
            int x = board_origin_x + (int) currentChess.getY()*chess_w - chess_w/2;
            g.drawImage(currentImg,x,y,chess_w,chess_h,this);
        }

        g.setColor(c);
    }


    public void startGame(boolean isFirst) {
        if (start_game == true) {
            return;
        }
        start_game = true;
        firstPlay = isFirst;
        if (firstPlay == false) {
            PutChess(9,9);
            repaint();
        }
    }

    private void setWin(char turn) {
        if (turn == 'b') {
            blackWin = true;
        } else {
            whiteWin = true;
        }
    }

    private boolean PutChess(int r, int c) {
        if (start_game == false) return false;

        if (board[r][c] == 0) {
            currentChess.setLocation(r, c, states[nextState]);
            board[r][c] = nextState+1;
            allChess.add(new ChessInfo((int) currentChess.getX(),(int) currentChess.getY(), currentChess.getState()));
            for (int i = 0; i < winsWayCount; ++i) {
                if (winsArr[r][c][i] == true) {
                    if (states[nextState] == 'b') {
                        blackWinsWayStatisticArr[i]++;
                    } else {
                        whiteWinsWayStatisticArr[i]++;
                    }
                    if (blackWinsWayStatisticArr[i] >= 5 || whiteWinsWayStatisticArr[i] >= 5) {
                        setWin(states[nextState]);
                    }
                }
            }
            nextState = (nextState+1) % statesCount;
            chessCount++;
            return true;
        }
        return false;

    }
    public void roolBackStepAndPain() {
        rollBackAStep();
        repaint();
    }

    private void rollBackAStep() {
        if (chessCount > 0) {
            ChessInfo temp = allChess.pollLast();
            board[(int) temp.getX()][(int) temp.getY()] = 0;
            currentChess = allChess.peekFirst();
            boolean haswin = false;
            for (int i = 0; i < winsWayCount; ++i) {
                if (winsArr[(int) temp.getX()][(int) temp.getY()][i] == true) {
                    if (temp.getState() == 'b') {
                        blackWinsWayStatisticArr[i]--;
                    } else {
                        whiteWinsWayStatisticArr[i]--;
                    }
                    if (blackWinsWayStatisticArr[i] >=5 || whiteWinsWayStatisticArr[i] >= 5) {
                        haswin = true;
                    }
                }
            }
            if (haswin == false) {
                blackWin = whiteWin = false;
            }

            nextState = (nextState+1) % statesCount;
            chessCount--;

        }
    }

    class PutAChessListener extends MouseAdapter {
        @Override
        public void mousePressed(MouseEvent e) {
            try {
                int x = e.getX() - PlayBoardPanel.board_origin_x;
                int y = e.getY() - PlayBoardPanel.board_origin_y;

                int c = (x+PlayBoardPanel.chess_w/2)/PlayBoardPanel.chess_w;
                int r = (y+PlayBoardPanel.chess_h/2)/PlayBoardPanel.chess_h;

                if (PutChess(r,c)) {
                    System.out.println("Debug:" + r + " " + c);
                    repaint();
                    MinMaxSearch();
                }

            } catch (Exception ee) {
                System.out.println(ee.getStackTrace());
            }

        }
    }



}
