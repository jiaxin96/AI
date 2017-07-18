package info.gridworld.maze;

import info.gridworld.actor.Actor;
import info.gridworld.actor.Bug;
import info.gridworld.actor.Flower;
import info.gridworld.actor.Rock;
import info.gridworld.grid.*;

import java.awt.Color;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Stack;

import javax.swing.JOptionPane;

/**
 * A <code>MazeBug</code> can find its way in a maze. <br />
 * The implementation of this class is testable on the AP CS A and AB exams.
 */
public class MazeBug extends Bug {
	public Location next;
	public Location last;
	
	public boolean isEnd = false;
	public Stack<Location> crossLocation = new Stack<Location>();
	public HashSet<Location> visited = new HashSet<>();
	public Integer stepCount = 0;
	private Location origian;
	boolean hasShown = false;//final message has been shown
	private HashMap<Integer,Integer> dirs = new HashMap<Integer, Integer>();
	/**
	 * Constructs a box bug that traces a square of a given side length
	 * 
	 * @param length
	 *            the side length
	 */
	public MazeBug() {
		setColor(Color.GREEN);
		last = new Location(0, 0);
		dirs.put(Location.EAST, 0);
		dirs.put(Location.SOUTH, 0);
		dirs.put(Location.WEST, 0);
		dirs.put(Location.NORTH, 0);
	}

	/**
	 * Moves to the next location of the square.
	 */
	public void act() {
		boolean willMove = canMove();
		if (isEnd == true) {
		//to show step count when reach the goal		
			if (hasShown == false) {
				String msg = stepCount.toString() + " steps";
				JOptionPane.showMessageDialog(null, msg);
				hasShown = true;
			}
		} else if (willMove) {
			move();
			//increase step count when move 
			stepCount++;
		} 
	}

	/**
	 * Find all positions that can be move to.
	 * 
	 * @param loc
	 *            the location to detect.
	 * @return List of positions.
	 */
	public ArrayList<Location> getValid(Location loc) {
		Grid<Actor> gr = getGrid();
		if (gr == null)
			return null;
		
		ArrayList<Location> valid = new ArrayList<Location>();

		
//		for (int dir : dirs) {
//			Location temp = loc.getAdjacentLocation(dir);
//			if (gr.isValid(temp) && !visited.contains(temp)) {
//				valid.add(temp);
//			}
//		}
		
		List<Map.Entry<Integer,Integer>> trendDirs = fixOrder();
		
		for (int i = 0; i < trendDirs.size(); ++i) {
			Location temp = loc.getAdjacentLocation(trendDirs.get(i).getKey());
			if (gr.isValid(temp) && !visited.contains(temp)) {
				valid.add(temp);
				dirs.replace(trendDirs.get(i).getKey(), trendDirs.get(i).getValue()+1);
			}
		}
		
		return valid;
	}



	private List<Map.Entry<Integer,Integer>> fixOrder() {
		// TODO Auto-generated method stub
		List<Map.Entry<Integer,Integer>> list =
			    new ArrayList<Map.Entry<Integer,Integer>>(dirs.entrySet());
		Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
		    public int compare(Map.Entry<Integer, Integer> o1,
		            Map.Entry<Integer, Integer> o2) {
		        return (o2.getValue() - o1.getValue());
		    }
		});
		return list;
	}

	/**
	 * Tests whether this bug can move forward into a location that is empty or
	 * contains a flower.
	 * 
	 * @return true if this bug can move.
	 */
	
	private boolean stepback() {
		if (stepCount == 0) {
			turn();
			turn();
			return false;
		}
		if(getLocation() == origian) {
			return false;
		}
		last = crossLocation.pop();
		next = crossLocation.pop();
		return true;
	}
	
	public boolean canMove() {
		
		if (stepCount == 0) {
			origian = getLocation();
		}
		
		visited.add(getLocation());
		crossLocation.add(getLocation());
		
		Grid<Actor> gr = getGrid();
		ArrayList<Location> nullLoc = new ArrayList<>();
		
		for (Location loc : getValid(getLocation())) {
			Actor actor = gr.get(loc);
			if (actor == null) {
				nullLoc.add(loc);
			} else if (actor instanceof Rock) {
				if (actor.getColor().equals(Color.RED)) {
					next = loc;
					isEnd = true;
					last = getLocation();
					return true;
				}
			}
		}
		
		if (nullLoc.size() == 0) {
			return stepback();
		}
		
		next = nullLoc.get(0);
		last = getLocation();
		return true;
		
	}
	/**
	 * Moves the bug forward, putting a flower into the location it previously
	 * occupied.
	 */
	public void move() {
		Grid<Actor> gr = getGrid();
		if (gr == null)
			return;
		Location loc = getLocation();
		if (gr.isValid(next)) {
			setDirection(getLocation().getDirectionToward(next));
			moveTo(next);
		} else
			removeSelfFromGrid();
		Flower flower = new Flower(getColor());
		flower.putSelfInGrid(gr, loc);
	}
}
