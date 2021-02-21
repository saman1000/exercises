package practice.bricks;

/**
 * We want to make a row of bricks that is goal inches long. We have a number of
 * small bricks (1 inch each) and big bricks (5 inches each). Return true if it
 * is possible to make the goal by choosing from the given bricks. This is a
 * little harder than it looks and can be done without any loops.
 * <p>
 * makeBricks(3, 1, 8) → true
 * makeBricks(3, 1, 9) → false
 * makeBricks(3, 2, 10) → true
 */
public class BrickCalculator {

    private static final int smallUnit = 1;
    private static final int bigUnit = 5;

    public boolean enoughBricks(int small, int big, int goal) {
        return makeBricks(small, big, goal);
    }

    private boolean makeBricks(int small, int big, int goal) {
        boolean result = BrickCalculator.smallUnit * small >= goal;

        int num = goal / BrickCalculator.bigUnit;
        if (num <= big) {
            result = (goal % BrickCalculator.bigUnit) <= small;
        }

        return result;
    }

}
