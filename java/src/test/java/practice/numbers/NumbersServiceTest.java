package practice.numbers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.List;
import java.util.stream.Stream;

class NumbersServiceTest {

    private final NumbersService numbersService = new NumbersService();

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
        Assertions.assertEquals(expectedOddNumbers, oddNumberList.size());
    }

    @ParameterizedTest
    @MethodSource("flavorsStream")
    public void testwhatFlavors(List<Integer> cost, int money, List<Integer> expectedFlavors) {
        List<Integer> actualFlavorsd = numbersService.whatFlavors(cost, money);
        Assertions.assertEquals(expectedFlavors, actualFlavorsd);
    }

    private static Stream<Arguments> flavorsStream() {
        return Stream.of(
                Arguments.of(List.of(1, 2, 3, 5, 6), 5, List.of(2, 3))
        );
    }

    @ParameterizedTest
    @MethodSource("removableIndicesStream")
    public void testGetRemovableIndices(String str1, String str2, List<Integer> expectedRemovableIndices) {
        Assertions.assertEquals(
                expectedRemovableIndices,
                numbersService.getRemovableIndices(str1, str2)
        );
    }

    private static Stream<Arguments> removableIndicesStream() {
        return Stream.of(
                Arguments.of("aba", "ba", List.of(0)),
                Arguments.of("abab", "aba", List.of(3)),
                Arguments.of("aab", "ab", List.of(0, 1)),
                Arguments.of("aabaab", "aabaa", List.of(5))
        );
    }
}