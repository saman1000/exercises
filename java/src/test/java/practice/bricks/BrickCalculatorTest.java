package practice.bricks;

import org.junit.Assert;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class BrickCalculatorTest {

    private final BrickCalculator brickCalculator = new BrickCalculator();

    @ParameterizedTest
    @CsvSource({
            "3, 1, 8, true",
            "3, 0, 3, true",
            "0, 2, 10, true",
            "3, 1, 9, false",
            "3, 2, 10, true",
            "3, 6, 22, true",
            "8, 0, 7, true",
            "1, 6, 22, false",
            "0, 1, 5, true",
            "2, 1, 8, false",
            "4, 3000, 15003, true"
    })
    public void testEnoughBricks(int small, int big, int goal, boolean enough) {
        Assert.assertEquals(brickCalculator.enoughBricks(small, big, goal), enough);
    }
}