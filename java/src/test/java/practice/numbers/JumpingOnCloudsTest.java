package practice.numbers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.List;
import java.util.stream.Stream;

class JumpingOnCloudsTest {

    private final JumpingOnclouds jumpingOnclouds = new JumpingOnclouds();

    @ParameterizedTest
    @MethodSource("cloudsTestStream")
    public void testGetOddListFunctioningCorrectly(List<Integer> listOfClouds, int expectedJumps) {
        int actualJumps = jumpingOnclouds.jumpingOnClouds(listOfClouds);
        Assertions.assertEquals(expectedJumps, actualJumps);
    }

    private static Stream<Arguments> cloudsTestStream() {
        return Stream.of(
                Arguments.of(List.of(1, 0, 1, 0, 0, 0), 3),
                Arguments.of(List.of(0, 0, 1, 0, 0, 1, 0), 4),
                Arguments.of(List.of(0, 0, 0, 1, 0, 0), 3),
                Arguments.of(List.of(0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0), 28),
                Arguments.of(List.of(0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), 53)
        );
    }
}