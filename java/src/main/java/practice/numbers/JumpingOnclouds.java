package practice.numbers;

import java.util.List;

public class JumpingOnclouds {

    /**
     * There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.
     * <p>
     * For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
     *
     * @param clouds list of clouds, 0 represents cumulus and 1 indicates thunderheads
     * @return
     * example: 0 0 1 0 0 1 0 should produce 4
     * 0 0 0 1 0 0 should produce 3
     */
    public int jumpingOnClouds(List<Integer> clouds) {
        // Write your code here
        int numberOfJumps = -1;
        int consecutiveCumulusClouds = 0;

        for (int aCloud : clouds) {
            if (aCloud == 0) {
                numberOfJumps++;
                consecutiveCumulusClouds++;
            } else {
                consecutiveCumulusClouds = 0;
            }
            if (consecutiveCumulusClouds == 3) {
                numberOfJumps--;
                consecutiveCumulusClouds = 0;
            }
        }

        return numberOfJumps;

        /*
          this algorithm is less efficient if LinkedList is used
          because get(i) → O(n) which results in O(n²) which is bad at scale
         */
//        int jumps = 0;
//        for (int i = 0; i < clouds.size() - 1; ) {
//            if (i + 2 < clouds.size() && clouds.get(i + 2) == 0) {
//                i += 2;
//            } else {
//                i += 1;
//            }
//            jumps++;
//        }
//        return jumps;
    }

}
