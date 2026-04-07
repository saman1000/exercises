package practice.numbers;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class NumbersService {

    public List<Integer> getOddList(int leftNumber, int rightNumber) {
        return IntStream.rangeClosed(leftNumber, rightNumber).filter(i -> i % 2 == 1).boxed().collect(Collectors.toList());
    }

    /**
     * Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream.
     * On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.
     * <p>
     * Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor,
     * help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money
     * during each visit. ID numbers are the 1- based index number associated with a .
     * For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny
     * purchase as two space-separated integers on a new line. You must print the
     * smaller ID first and the larger ID second.
     * <p>
     * Example
     * <p>
     * <p>
     * <p>
     * They would purchase flavor ID's  and  for a cost of . Use  based indexing for your response.
     * <p>
     * Note:
     * <p>
     * Two ice creams having unique IDs  and  may have the same cost (i.e., ).
     * There will always be a unique solution.
     * Function Description
     * <p>
     * Complete the function whatFlavors in the editor below.
     * <p>
     * whatFlavors has the following parameter(s):
     * <p>
     * int cost[n] the prices for each flavor
     * int money: the amount of money they have to spend
     * Prints
     * <p>
     * int int: the indices of the two flavors they will purchase as two space-separated integers on a line
     * Input Format
     * <p>
     * The first line contains an integer, , the number of trips to the ice cream parlor.
     * <p>
     * Each of the next  sets of  lines is as follows:
     * <p>
     * The first line contains .
     * The second line contains an integer, , the size of the array .
     * The third line contains  space-separated integers denoting the .
     * Constraints
     * <p>
     * Sample Input
     * <p>
     * STDIN       Function
     * -----       --------
     * 2           t = 2
     * 4           money = 4
     * 5           cost[] size n = 5
     * 1 4 5 3 2   cost = [1, 4, 5, 3, 2]
     * 4           money = 4
     * 4           cost[] size n = 4
     * 2 2 4 3     cost = [2, 2, 4, 3]
     * Sample Output
     * <p>
     * 1 4
     * 1 2
     * Explanation
     * <p>
     * Sunny and Johnny make the following two trips to the parlor:
     * <p>
     * The first time, they pool together  dollars. There are five flavors available that day and flavors  and  have a total cost of .
     * The second time, they pool together  dollars. There are four flavors available that day and flavors  and  have a total cost of .
     * <p>
     * [1 2 3 5 6], 5 --> 2 3
     *
     */
    public Optional<List<Integer>> whatFlavors(List<Integer> cost, int money) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < cost.size(); i++) {
            int current = cost.get(i);
            int complement = money - current;

            if (map.containsKey(complement)) {
                return Optional.of(Arrays.asList(map.get(complement) + 1, i + 1));
            }

            map.put(current, i);
        }

        return Optional.empty();
    }


    /*
     * Complete the 'getRemovableIndices' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. STRING str1
     *  2. STRING str2
     */
    public List<Integer> getRemovableIndices(String str1, String str2) {
        // Write your code here
        int n = str1.length();
        int m = str2.length();
        // Quick check
        if (n != m + 1) {
            return List.of(-1);
        }

        int prefixLength = 0;
        while (prefixLength < m && prefixLength < n && str1.charAt(prefixLength) == str2.charAt(prefixLength)) {
            prefixLength++;
        }

        int suffixLength = 0;
        while (suffixLength < m && suffixLength < n - prefixLength - 1 && str1.charAt(n - 1 - suffixLength) == str2.charAt(m - 1 - suffixLength)) {
            suffixLength++;
        }

        // Check if we can remove exactly one character
        if (prefixLength + suffixLength == m) {
            // The character at position prefixLength can be removed
            List<Integer> result = new ArrayList<>();
            // Check for consecutive identical characters
            char charToRemove = str1.charAt(prefixLength);
            int start = prefixLength;
            int end = prefixLength;
            // Find all consecutive identical characters
            while (start > 0 && str1.charAt(start - 1) == charToRemove) {
                start--;
            }
            while (end < n - 1 && str1.charAt(end + 1) == charToRemove) {
                end++;
            }

            // Add all possible indices
            for (int i = start; i <= end; i++) {
                result.add(i);
            }

            return result;
        }

        return List.of(-1);
    }

    public int alternate(String s) {
        Set<Character> unique = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet());

        int maxLength = 0;

        List<Character> chars = new ArrayList<>(unique);

        for (int i = 0; i < chars.size(); i++) {
            for (int j = i + 1; j < chars.size(); j++) {
                char c1 = chars.get(i);
                char c2 = chars.get(j);

                String filtered = s.chars()
                        .mapToObj(c -> (char) c)
                        .filter(c -> c == c1 || c == c2)
                        .map(String::valueOf)
                        .collect(Collectors.joining());

                if (isValidAlternating(filtered)) {
                    maxLength = Math.max(maxLength, filtered.length());
                }
            }
        }

        return maxLength;
    }

    private boolean isValidAlternating(String s) {
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                return false;
            }
        }
        return s.length() > 1;
    }

    /**
     *
     * @param values list of integers
     * @param medianCount number of consecutive integers for which we need the median for
     * @return List of median values. An empty list if length of values is less than medianCount
     */
    public List<Float> calculateMedians(List<Integer> values, int medianCount) {
        List<Float> medianList = new LinkedList<>();

        List<Integer> tmpList;
        int lowerMedianIndex1 = medianCount / 2;
        int higherMedianIndex2 = lowerMedianIndex1 - 1;
        for (int index = 0; index <= values.size() - medianCount; index++) {
            tmpList = new ArrayList<>(values.subList(index, index + medianCount));
            Collections.sort(tmpList);
            if (medianCount % 2 == 0) {
                medianList.add(
                        (tmpList.get(lowerMedianIndex1) + tmpList.get(higherMedianIndex2)) / 2f
                );
            } else {
                medianList.add((float) tmpList.get(lowerMedianIndex1));
            }
        }

        return medianList;
    }

    public List<Float> medianSlidingWindow(int[] nums, int k) {
        List<Float> result = new ArrayList<>();

        PriorityQueue<Integer> low = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> high = new PriorityQueue<>();

        Map<Integer, Integer> delayed = new HashMap<>();
        int lowSize = 0, highSize = 0;

        for (int i = 0; i < nums.length; i++) {
            if (low.isEmpty() || nums[i] <= low.peek()) {
                low.offer(nums[i]);
                lowSize++;
            } else {
                high.offer(nums[i]);
                highSize++;
            }

            // balance
            if (lowSize > highSize + 1) {
                high.offer(low.poll());
                lowSize--;
                highSize++;
            } else if (lowSize < highSize) {
                low.offer(high.poll());
                lowSize++;
                highSize--;
            }

            if (i >= k - 1) {
                // median
                if (k % 2 == 0) {
                    result.add((low.peek() + high.peek()) / 2f);
                } else {
                    result.add((float) low.peek());
                }

                int toRemove = nums[i - k + 1];
                delayed.put(toRemove, delayed.getOrDefault(toRemove, 0) + 1);

                if (toRemove <= low.peek()) lowSize--;
                else highSize--;

                // cleanup heaps
                while (!low.isEmpty() && delayed.getOrDefault(low.peek(), 0) > 0) {
                    delayed.put(low.peek(), delayed.get(low.peek()) - 1);
                    low.poll();
                }

                while (!high.isEmpty() && delayed.getOrDefault(high.peek(), 0) > 0) {
                    delayed.put(high.peek(), delayed.get(high.peek()) - 1);
                    high.poll();
                }
            }
        }

        return result;
    }
}
