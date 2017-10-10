import java.awt.*;

/**
 * Created by jx on 7/6/17.
 */
public class ChessInfo extends Point {
    // n  :  nothing
    // b  :  black
    // w  :  white
    private  char state = 'n';

    public ChessInfo() {
        state = 'n';
    }

    public ChessInfo(int x,int y) {
        super(x,y);
        state = 'n';
    }

    public ChessInfo(int x, int y, char state) {
        super(x,y);
        this.state = state;
    }

    public void setLocation(int x, int y, char state) {
        super.setLocation(x, y);
        this.state = state;
    }

    public char getState() {
        return state;
    }

    public void setState(char state) {
        this.state = state;
    }
}
