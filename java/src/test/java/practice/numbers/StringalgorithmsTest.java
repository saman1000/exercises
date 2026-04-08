package practice.numbers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import practice.strings.StringAlgorithms;

class StringalgorithmsTest {

    private final StringAlgorithms stringAlgorithms = new StringAlgorithms();

    @ParameterizedTest
    @CsvSource({
            "aba, 10, 7",
            "a, 1000000000000, 1000000000000"
    })
    public void testGetOddListFunctioningCorrectly(String s, long n, long expectedValue) {
        long actualValue = stringAlgorithms.repeatedString(s, n);
        Assertions.assertEquals(expectedValue, actualValue);
    }
}