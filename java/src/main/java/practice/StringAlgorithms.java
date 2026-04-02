package practice;

public class StringAlgorithms {

    /**
     * There is a string, s, of lowercase English letters that is repeated infinitely many times.
     * Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
     *
     */
    public long repeatedString(String string, long firstCharacters) {
        // Write your code here
        if (string == null || string.isEmpty()) {
            return 0L;
        }

        long length = string.length();

        // Count 'a' in the original string
        long repeatedLetters = string.chars().filter(ch -> ch == 'a').count();

        // Number of full repeats of s in n characters
        long fullRepeats = firstCharacters / length;

        // Count 'a's in full repeats
        repeatedLetters *= fullRepeats;

        // Count 'a's in the remaining partial repeat
        long remaining = firstCharacters % length;
        repeatedLetters += string.chars().limit(remaining).filter(ch -> ch == 'a').count();

        return repeatedLetters;
    }

}
