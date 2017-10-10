import javafx.embed.swing.JFXPanel;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.GroupLayout;
/*
 * Created by JFormDesigner on Wed Jul 05 18:10:16 CST 2017
 */



/**
 * @author Brainrain
 */
public class MainFrame extends JFrame {

    public static void main(String[] args) {
        MainFrame mainFrame = new MainFrame();
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public MainFrame() {
        initComponents();
        Toolkit tk = Toolkit.getDefaultToolkit();
        this.setLocation((tk.getScreenSize().width - this.getWidth())/2, (tk.getScreenSize().height - this.getWidth())/2);
        this.setVisible(true);
        this.setResizable(false);
    }

    private void HelpMenuAboutMouseClicked(MouseEvent e) {
        // TODO add your code here
        AboutFrame aboutFrame = new AboutFrame();
        aboutFrame.setVisible(true);
    }

    private void firststartMousePressed(MouseEvent e) {
        // TODO add your code here
        BoardPanel.startGame(true);
    }

    private void BackHandMousePressed(MouseEvent e) {
        // TODO add your code here
        BoardPanel.startGame(false);
    }

    private void roolBackMousePressed(MouseEvent e) {
        // TODO add your code here
        BoardPanel.roolBackStepAndPain();

    }

    private void initComponents() {
        // JFormDesigner - Component initialization - DO NOT MODIFY  //GEN-BEGIN:initComponents
        menuBar1 = new JMenuBar();
        menu1 = new JMenu();
        menuItem1 = new JMenuItem();
        menuItem2 = new JMenuItem();
        menuItem3 = new JMenuItem();
        menu2 = new JMenu();
        menuItem4 = new JMenuItem();
        panel1 = new JPanel();
        label1 = new JLabel();
        label2 = new JLabel();
        label5 = new JLabel();
        label6 = new JLabel();
        label7 = new JLabel();
        BoardPanel = new PlayBoardPanel();

        //======== this ========
        Container contentPane = getContentPane();

        //======== menuBar1 ========
        {

            //======== menu1 ========
            {
                menu1.setText("Game");

                //---- menuItem1 ----
                menuItem1.setText("FirstStart");
                menuItem1.addMouseListener(new MouseAdapter() {
                    @Override
                    public void mousePressed(MouseEvent e) {
                        firststartMousePressed(e);
                    }
                });
                menu1.add(menuItem1);

                //---- menuItem2 ----
                menuItem2.setText("Backhand");
                menuItem2.addMouseListener(new MouseAdapter() {
                    @Override
                    public void mousePressed(MouseEvent e) {
                        BackHandMousePressed(e);
                    }
                });
                menu1.add(menuItem2);

                //---- menuItem3 ----
                menuItem3.setText("BackStep");
                menuItem3.addMouseListener(new MouseAdapter() {
                    @Override
                    public void mousePressed(MouseEvent e) {
                        roolBackMousePressed(e);
                    }
                });
                menu1.add(menuItem3);
            }
            menuBar1.add(menu1);

            //======== menu2 ========
            {
                menu2.setText("Help");

                //---- menuItem4 ----
                menuItem4.setText("About");
                menuItem4.addMouseListener(new MouseAdapter() {
                    @Override
                    public void mousePressed(MouseEvent e) {
                        HelpMenuAboutMouseClicked(e);
                    }
                });
                menu2.add(menuItem4);
            }
            menuBar1.add(menu2);
        }
        setJMenuBar(menuBar1);

        //======== panel1 ========
        {

            //---- label1 ----
            label1.setText("Person1:");
            label1.setHorizontalAlignment(SwingConstants.CENTER);

            //---- label2 ----
            label2.setText("Person2:");
            label2.setHorizontalAlignment(SwingConstants.CENTER);

            //---- label5 ----
            label5.setText("Step:");

            //---- label6 ----
            label6.setText("Back");

            //---- label7 ----
            label7.setText("Gobang");
            label7.setHorizontalAlignment(SwingConstants.CENTER);
            label7.setFont(new Font("Cantarell", Font.BOLD, 23));
            label7.setEnabled(false);

            //======== BoardPanel ========
            {
                BoardPanel.setPreferredSize(new Dimension(600, 600));

                GroupLayout BoardPanelLayout = new GroupLayout(BoardPanel);
                BoardPanel.setLayout(BoardPanelLayout);
                BoardPanelLayout.setHorizontalGroup(
                    BoardPanelLayout.createParallelGroup()
                        .addGap(0, 600, Short.MAX_VALUE)
                );
                BoardPanelLayout.setVerticalGroup(
                    BoardPanelLayout.createParallelGroup()
                        .addGap(0, 600, Short.MAX_VALUE)
                );
            }

            GroupLayout panel1Layout = new GroupLayout(panel1);
            panel1.setLayout(panel1Layout);
            panel1Layout.setHorizontalGroup(
                panel1Layout.createParallelGroup()
                    .addGroup(panel1Layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(BoardPanel, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                        .addGap(29, 29, 29)
                        .addGroup(panel1Layout.createParallelGroup()
                            .addGroup(panel1Layout.createSequentialGroup()
                                .addGroup(panel1Layout.createParallelGroup()
                                    .addGroup(panel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING, false)
                                        .addComponent(label2, GroupLayout.DEFAULT_SIZE, 67, Short.MAX_VALUE)
                                        .addComponent(label1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                    .addGroup(panel1Layout.createSequentialGroup()
                                        .addComponent(label5)
                                        .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                                        .addComponent(label6)))
                                .addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                            .addGroup(panel1Layout.createSequentialGroup()
                                .addComponent(label7, GroupLayout.DEFAULT_SIZE, 83, Short.MAX_VALUE)
                                .addContainerGap())))
            );
            panel1Layout.setVerticalGroup(
                panel1Layout.createParallelGroup()
                    .addGroup(panel1Layout.createSequentialGroup()
                        .addGap(123, 123, 123)
                        .addComponent(label1, GroupLayout.PREFERRED_SIZE, 48, GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(label2, GroupLayout.PREFERRED_SIZE, 55, GroupLayout.PREFERRED_SIZE)
                        .addGap(98, 98, 98)
                        .addGroup(panel1Layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                            .addComponent(label5)
                            .addComponent(label6))
                        .addGap(18, 18, 18)
                        .addComponent(label7, GroupLayout.DEFAULT_SIZE, 201, Short.MAX_VALUE)
                        .addContainerGap(28, Short.MAX_VALUE))
                    .addGroup(panel1Layout.createSequentialGroup()
                        .addComponent(BoardPanel, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 9, Short.MAX_VALUE))
            );
        }

        GroupLayout contentPaneLayout = new GroupLayout(contentPane);
        contentPane.setLayout(contentPaneLayout);
        contentPaneLayout.setHorizontalGroup(
            contentPaneLayout.createParallelGroup()
                .addGroup(contentPaneLayout.createSequentialGroup()
                    .addContainerGap()
                    .addComponent(panel1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                    .addContainerGap(43, Short.MAX_VALUE))
        );
        contentPaneLayout.setVerticalGroup(
            contentPaneLayout.createParallelGroup()
                .addComponent(panel1, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        pack();
        setLocationRelativeTo(getOwner());
        // JFormDesigner - End of component initialization  //GEN-END:initComponents
    }

    // JFormDesigner - Variables declaration - DO NOT MODIFY  //GEN-BEGIN:variables
    private JMenuBar menuBar1;
    private JMenu menu1;
    private JMenuItem menuItem1;
    private JMenuItem menuItem2;
    private JMenuItem menuItem3;
    private JMenu menu2;
    private JMenuItem menuItem4;
    private JPanel panel1;
    private JLabel label1;
    private JLabel label2;
    private JLabel label5;
    private JLabel label6;
    private JLabel label7;
    private PlayBoardPanel BoardPanel;
    // JFormDesigner - End of variables declaration  //GEN-END:variables
}
