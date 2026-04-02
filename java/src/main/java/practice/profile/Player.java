package practice.profile;

/**
 * pick the packages from the heaviest to the lightest one
 *
 *  that takes 3 integer arguments: weight0, weight1 and weight2.
 *  These values represent the weight of the packages available on
 *  the conveyor belts with respective index 0, 1 and 2. When
 *  a conveyor belt is empty, the value is 0.
 */
class Player {

    public static int solve(int weight0, int weight1, int weight2) {
        // Write your code here
        // To debug: System.err.println("Debug messages...");
        int index = weight1 > weight0 ? 1 : 0;
        if (weight2 > weight1 && weight2 > weight0) {
            index = 2;
        }

        return index;
    }

    public static void main(String args[]) {
        System.out.println(String.format("%d should be %d", 2, solve(85, 70, 100)));
        System.out.println(String.format("%d should be %d", 2, solve(70, 80, 100)));
        System.out.println(String.format("%d should be %d", 0, solve(170, 80, 100)));
        System.out.println(String.format("%d should be %d", 0, solve(80, 70, 0)));
        System.out.println(String.format("%d should be %d", 0, solve(70, 70, 70)));
        System.out.println(String.format("%d should be %d", 0, solve(0, 0, 0)));
    }
}
