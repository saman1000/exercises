package practice.numbers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.List;
import java.util.stream.Stream;

class PairingServiceTest {

    private final PairingService pairingService = new PairingService();

    @ParameterizedTest
    @MethodSource("pairsTestStream")
    public void testGetOddListFunctioningCorrectly(List<Integer> listOfNumbers, int expectedPairs) {
        int actualPairs = pairingService.sockMerchantnumberOfPairs(listOfNumbers);
        Assertions.assertEquals(expectedPairs, actualPairs);
    }

    private static Stream<Arguments> pairsTestStream() {
        return Stream.of(
                Arguments.of(List.of(2, 1), 0),
                Arguments.of(List.of(10, 20, 20, 10, 10, 30, 50, 10, 20), 3),
                Arguments.of(List.of(), 0)
        );
    }
}