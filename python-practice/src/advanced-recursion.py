def permute(nums):
    def backtrack(first=0):
        if first == len(nums):
            result.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first] # Swap numbers
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first] # Swap them back to reset the state

    result = []
    backtrack()
    return result

def lexicographical_permutation(nums):
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

    result = []
    nums.sort()
    backtrack([], nums)
    return result

def all_combinations(s):
    def backtrack(path, remaining):
        if path:
            s_path = "".join(path)
            if s_path not in result:
                result.add(s_path)
                result.add(s_path[::-1])
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

    result = set()
    s = sorted(s)
    backtrack([], s)
    return result

def generate_parentheses(n: int) -> list[str]:
    def backtrack(open_p=0, close_p=0):
        if open_p == n and close_p == n and s:
            result.append("".join(s))
            return
        if open_p < n:
            s.append('(')
            backtrack(open_p + 1, close_p)
            s.pop()
        if close_p < open_p:
            s.append(')')
            backtrack(open_p, close_p + 1)
            s.pop()

    # '(' is less than ')'
    result = []
    s = []
    backtrack()
    return result


def all_possible_cases(s):
    # TODO: implement the solution
    char_array = list(s)
    result = set()
    s_length = len(s)

    def backtrack(first=0):
        combination = "".join(char_array)
        if combination not in result:
            result.add(combination)
        for index in range(first, s_length):
            if not char_array[index].isalpha():
                continue
            char_array[index] = char_array[index].swapcase()
            backtrack(first + 1)
            char_array[index] = char_array[index].swapcase()

    backtrack()
    return result

def word_game(words):
    result = []
    word_length = len(words)

    def backtrack(index=0, path=[]):
        if index == word_length:
            result.append("".join(path))
            return
        for one_char in words[index]:
            path.append(one_char)
            backtrack(index + 1, path)
            path.pop()

    words = [sorted(w) for w in words]
    backtrack()
    return result

if __name__ == "__main__":
    # self.assertEqual(solution(['gh', 'ij', 'kl']), ['gik', 'gil', 'gjk', 'gjl', 'hik', 'hil', 'hjk', 'hjl'])
    print(word_game(['gh', 'ij', 'kl']))