package practice.profile;

import java.util.Arrays;
import java.util.List;

/**
 * Your company builds radioactivity sensors. You are responsible of their verification process. You know that when a sensor is failing, the value it outputs have big variatons on short time periods.
 * <p>
 * The input parameter values, a list of decimal numbers, contains the radioactivity measured by the sensor every second. The unit is arbitrary.
 * <p>
 * You want to count the quantity of "peaks" in these values, which would help you determine if the sensor fails.
 * When a value is at least 5 units higher than its two neighbors, it's a "top peak".
 * When a value is at least 5 units lower than its two neighbors, it's a "bottom peak".
 * You must return an integer: the total number of top peaks and bottom peaks.
 * The first and last elements of the list values can never be peaks.
 * <p>
 * values is always defined (it is never null, None, etc.). It contains between 0 and 20 values.
 * <p>
 * The radioactivity values are between 0 and 100.
 * Example
 * With these values :
 * 8 ; 10.7 ; 17.1 ; 11.2 ; 13.5 ; 9.9 ; 14.9 ; 9.4 ; 9.4 ; 3.1 ; 12.7
 */
public class Redioactivity {


    /**
     * @param values The radioactivity values measured by the sensor
     * @return The total number of top peaks and bottom peaks found in the radioactivity values.
     */
    public static int countPeaks(List<Double> values) {
        // Write your code here
        // To debug: System.err.println("Debug messages...");

        int length = values.size();
        Double[] readingsArray = values.toArray(new Double[length]);
        int numberOfPeaks = 0;
        for (int index = 1; index < length - 1; index++) {
            double leftDiff = readingsArray[index] - readingsArray[index - 1];
            double rightDiff = readingsArray[index] - readingsArray[index + 1];
            if (leftDiff * rightDiff < 0)
                continue;
            leftDiff = Math.abs(leftDiff);
            rightDiff = Math.abs(rightDiff);
            if (
                    (leftDiff == 5d && rightDiff > 5D)
                    || (leftDiff > 5D && rightDiff > 5D)
                    || (leftDiff > 5D && rightDiff == 5D)
            ) {
                numberOfPeaks++;
            }
        }

        return numberOfPeaks;
    }

    public static void main(String[] args) {
        System.out.println(countPeaks(Arrays.asList(8D, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7)) + " = " + 3);
        System.out.println(countPeaks(Arrays.asList(81.3, 80.3, 75.3, 80.3, 85.2, 90.2, 95.2, 90.2, 89.1, 88.8)) + " = " + 2);
    }
}
