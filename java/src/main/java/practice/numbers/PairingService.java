package practice.numbers;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

public class PairingService {

    /**
     *
     * 9, [10, 20, 20, 10, 10, 30, 50, 10, 20] should return 3
     */
//    public int sockMerchantnumberOfPairsOldJava(int totalNumbers, List<Integer> listOfNumbers) {
//        // Write your code here
//        int numberOfPairs = 0;
//        Set<Integer> seen = new HashSet<>();
//        for (int n : listOfNumbers)
//            if (!seen.add(n)) {
//                numberOfPairs++;
//                seen.remove(n);
//            }
//        return numberOfPairs;
//    }

    public int sockMerchantnumberOfPairs(List<Integer> listOfNumbers) {
        // Write your code here
        return listOfNumbers.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.summingInt(e -> 1)))
                .values().stream()
                .mapToInt(count -> count / 2)
                .sum();
    }
}
