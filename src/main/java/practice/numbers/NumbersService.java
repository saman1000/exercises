package practice.numbers;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class NumbersService {

    public List<Integer> getOddList(int leftNumber, int rightNumber) {
        return IntStream
                .rangeClosed(leftNumber, rightNumber)
                .filter(i -> i % 2 == 1)
                .boxed()
                .collect(Collectors.toList());
    }
}
