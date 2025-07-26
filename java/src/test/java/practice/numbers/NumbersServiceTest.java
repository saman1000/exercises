package practice.numbers;

import org.junit.Assert;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class NumbersServiceTest {

    private NumbersService numbersService = new NumbersService();

    @ParameterizedTest
    @CsvSource({
            "1, 2, 1",
            "2, 10, 4",
            "0, 0, 0",
            "-1, 0, 0",
            "-10, -2, 0",
            "24, 3003, 1490"
    })
    public void testGetOddListFunctioningCorrectly(int leftNumber, int rightNumber, int expectedOddNumbers) {
        List<Integer> oddNumberList = numbersService.getOddList(leftNumber, rightNumber);
        Assert.assertEquals(expectedOddNumbers, oddNumberList.size());
    }
}