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
        Assertions.assertEquals(expectedFlavors, numbersService.whatFlavors(cost, money).orElse(null));
    }

    private static Stream<Arguments> flavorsStream() {
        return Stream.of(
                Arguments.of(List.of(1, 2, 3, 5, 6), 5, List.of(2, 3)),
                Arguments.of(List.of(1, 4, 5, 3, 2), 4, List.of(1, 4)),
                Arguments.of(List.of(2, 2, 4, 3), 4, List.of(1, 2)),
                Arguments.of(List.of(1, 3, 4, 6, 7, 9), 9, List.of(2, 4)),
                Arguments.of(List.of(1, 3, 4, 4, 6, 8), 8, List.of(3, 4)),
                Arguments.of(List.of(1, 2), 3, List.of(1, 2))
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

    @ParameterizedTest
    @MethodSource("integerList")
    public void testCalculateMedians(List<Integer> values, int medianCount, List<Float> expectedMedians) {
        Assertions.assertEquals(expectedMedians, numbersService.calculateMedians(values, medianCount));
        Assertions.assertEquals(expectedMedians, numbersService.medianSlidingWindow(
                values.stream().mapToInt(x -> (int) x).toArray(),
                medianCount));
    }

    private static Stream<Arguments> integerList() {
        return Stream.of(
                Arguments.of(List.of(1, 2, 3, 4), 3, List.of(2f, 3f)),
                Arguments.of(List.of(2, 3, 4, 2, 3, 6, 8, 4, 5), 3, List.of(3f, 3f, 3f, 3f, 6f, 6f, 5f)),
                Arguments.of(List.of(2, 3, 4, 2, 3, 6, 8, 4, 5), 4, List.of(2.5f, 3f, 3.5f, 4.5f, 5f, 5.5f))
        );
    }
}