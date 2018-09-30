package algoproblem;

import java.util.*;

/**
 * Created by Administrator on 2018/9/30.
 * @author  ch
 */
public class ReconstructItinerary {


    public static void main(String[] args) {

        String[][] tickets={{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
        Map<String, PriorityQueue<String>> targets = new HashMap<>();
        for (String[] ticket : tickets){
            System.out.println(ticket[0]+"_"+ticket[1]);
            targets.computeIfAbsent(ticket[0], k -> new PriorityQueue()).add(ticket[1]);
        }


        System.out.println(targets);

        ReconstructItinerary reconstructItinerary=new ReconstructItinerary();
        List<String> route =reconstructItinerary.findItinerary(tickets);
        System.out.println(route);
    }

    public List<String> findItinerary(String[][] tickets) {
        Map<String, PriorityQueue<String>> targets = new HashMap<>();
        for (String[] ticket : tickets)
            targets.computeIfAbsent(ticket[0], k -> new PriorityQueue()).add(ticket[1]);
        List<String> route = new LinkedList();
        Stack<String> stack = new Stack<>();
        stack.push("JFK");
        while (!stack.empty()) {
            while (targets.containsKey(stack.peek()) && !targets.get(stack.peek()).isEmpty())
                stack.push(targets.get(stack.peek()).poll());
            route.add(0, stack.pop());
        }
        return route;
    }
}
