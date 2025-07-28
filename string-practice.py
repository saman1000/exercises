def get_common_suffix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    max_counter = len(shortest)
    index = 1
    while index <= max_counter:
        for str in strs:
            if shortest[-index] != str[-index]:
                return shortest[len(shortest) - index + 1:]
        index += 1
    return shortest[len(shortest) - index + 1:]

def largest_common_prefix(words):
    # TODO: Implement this function to find the largest common prefix among the words in the array.
    if not words:
        return ""
    shortest = min(words, key=len)
    for index, one_char in enumerate(shortest):
        for one_word in words:
            if shortest[index] != one_word[index]:
                return shortest[:index]
    return shortest

def efficient_lcp(strs):
    # TODO: implement the solution here
    if not strs:
        return ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    index = 0
    while index < len(first) and index < len(last):
        if first[index] != last[index]:
            return first[:index]
        index += 1
    return first

def repeat_substring(s):
    # TODO: implement the function according to the task requirements.
    substring = ""
    if s:
        str_length = len(s)
        sub_length = int(str_length / 2)
        while sub_length > 0:
            if s[:sub_length] * int(str_length / sub_length) == s:
                return s[:sub_length]
            sub_length -= 1
    return substring

def find_most_common_substring(s: str, length: int) -> str:
    # TODO: implement the function
    str_length = len(s)
    all_subs = {}
    for i in range(str_length - length + 1):
        sub_str = s[i: i + length]
        if all_subs.get(sub_str) is None:
            all_subs[sub_str] = 1
        else:
            all_subs[sub_str] += 1
    substring = ""
    max_count = 0
    for sub, repetition in all_subs.items():
        if repetition > max_count:
            substring = sub
            max_count = repetition
        elif repetition == max_count:
            substring = min(substring, sub)
    return substring

if __name__ == "__main__":
    strs =["invitation", "invigorating", "invalid"]
    print(efficient_lcp(strs))
    strs = ["ptintroduction", "ptreduction", "ptproduction", "ptseduction"]
    print(efficient_lcp(strs))
    print(efficient_lcp(["floss", "flight", "floral"]))