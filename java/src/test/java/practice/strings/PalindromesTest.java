package practice.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class PalindromesTest {

    private final Palindromes palindromes = new Palindromes();

    @ParameterizedTest
    @CsvSource({
            "abab, 1, 4, 2",
            "aab, 1, 3, 1",
            "madamimadam, 4, 7, 2",
            "week, 1, 4, 2",
            "week, 2, 4, 1"
    })
    public void answerQueryTest(String text, int leftIndex, int rightIndex, int expectedPolidromes) {
        palindromes.initialize(text);
        Assertions.assertEquals(expectedPolidromes, palindromes.answerQuery(leftIndex, rightIndex));
    }

    @ParameterizedTest
    @CsvSource({
            "aba, 0, 2, true",
            "madamimadam, 0, 3, false",
            "madamimadam, 1, 3, true",
            "madamimadam, 7, 9, true",
            "ab, 0, 1, false",
            "week, 1, 3, true",
            "zz, 0, 1, true"
    })
    public void isPalidromeTest(String text, int leftIndex, int rightIndex, boolean expectedPalidromeResult) {
        palindromes.initialize(text);
        Assertions.assertEquals(expectedPalidromeResult, palindromes.isPalidrome(leftIndex, rightIndex));
    }
}