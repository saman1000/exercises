package practice.strings;

import java.util.HashMap;

public class Palindromes {

    private int[] prefixMask;

    private void buildPrefixMask(char[] fullString) {
        int n = fullString.length;
        prefixMask = new int[n + 1];

        for (int i = 0; i < n; i++) {
            int charBit = 1 << (fullString[i] - 'a'); // assuming lowercase letters
            prefixMask[i + 1] = prefixMask[i] ^ charBit;
        }
    }

    public void initialize(String s) {
        buildPrefixMask(s.toLowerCase().toCharArray());
    }

    public int answerQuery(int logicalLeftIndex, int logicalRightIndex) {
        int palidromesWithMaxChars = 0;

        for (int counter = 0; logicalLeftIndex - 1 + counter < logicalRightIndex - counter && palidromesWithMaxChars == 0; counter++) {
            int subLength = logicalRightIndex - logicalLeftIndex + 1 - counter;
            int leftIndex = logicalLeftIndex - 1;
            while (leftIndex + subLength - 1 < logicalRightIndex) {
                if (!isPalidrome(leftIndex, leftIndex + subLength - 1)) {
                    palidromesWithMaxChars = 0;
                    break;
                }
                palidromesWithMaxChars += 1;
                leftIndex += 1;
            }
        }

        return palidromesWithMaxChars;
    }

    public boolean isPalidrome(int startIndex, int endIndex) {
        int mask = prefixMask[endIndex + 1] ^ prefixMask[startIndex];

        // check if at most one bit is set
        return (mask & (mask - 1)) == 0;
    }
}
