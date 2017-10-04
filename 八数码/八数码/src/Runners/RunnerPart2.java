package Runners;

import java.io.IOException;

import jigsaw.Jigsaw;
import jigsaw.JigsawNode;

public class RunnerPart2 {
	/**测试脚本-2
	 * 实验任务二：利用启发式搜索，求解随机5*5拼图（24-数码问题）
	 * 注意：运行前要修改节点维数，将JigsawNode类中的dimension改为5
	 * 要求：不修改脚本内容，程序能够运行，且得出预期结果
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		
		// 检查节点维数是否为8
		if(JigsawNode.getDimension() != 3){
			System.out.print("节点维数不正确，请将JigsawNode类的维数dimension改为3");
			return;
		}
		
		// 一天也跑不完 8 * 8
		// 生成目标状态对象destNode: {25,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0};
		// JigsawNode destNode = new JigsawNode(new int[]{64,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,0});  		
		JigsawNode destNode = new JigsawNode(new int[]{9,1,2,3,4,5,6,7,8,0}); 
		
		// 生成随机初始状态对象startNode：将目标状态打散，生成可解的随机初始状态
		JigsawNode startNode = Jigsaw.scatter(destNode, 1000);
		// JigsawNode startNode = new JigsawNode(new int[]{4,6,1,7,0,4,3,2,5,8});

		// 生成jigsaw对象：设置初始状态节点startNode和目标状态节点destNode
		Jigsaw jigsaw = new Jigsaw(startNode, destNode);

		// 执行启发式搜索示例算法
		System.out.println("曼哈顿距离启发式：");
		jigsaw.ASearch(0);

		System.out.println("错子数启发式：");
		jigsaw.ASearch(1);

		
	}

}
