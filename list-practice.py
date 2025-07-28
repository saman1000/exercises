from typing import List


def anti_rotate_array(nums: List[int], k: int) -> None:
    # TODO: Implement anti-clockwise rotation of the array nums by k steps.
    separation_index = k % len(nums)
    index = 0
    for one_number in nums[separation_index:] + nums[:separation_index]:
        nums[index] = one_number
        index += 1

def shuffle_array(nums, k):
    # TODO: implement the function here
    remained = []
    index = 0
    length = len(nums)
    for sep_index in range(k - 1, length, k):
        remained += nums[index:sep_index]
        index = sep_index + 1
    if index < length:
        remained += nums[index:length]
    removed = nums[k - 1:len(nums):k]
    return remained + removed

def group_reverse(numbers, k):
    reversed_list = []
    index = 0
    for sep_index in range(0, len(numbers), k):
        reversed_list += reverse_list(numbers[index:sep_index])
        index = sep_index
    if len(reversed_list) < len(numbers):
        reversed_list += reverse_list(numbers[len(reversed_list):len(numbers)])

    return reversed_list

def reverse_list(nums: List[int]) -> List[int]:
    if nums is None or len(nums) == 0:
        return []
    return [nums[-1]] + reverse_list(nums[:-1])

def rearrange_array(nums):
    # TODO: implement the function.
    total_size = len(nums)
    quarter_size = int(total_size / 4)
    middle_part = nums[quarter_size:-quarter_size]
    first_quarter = nums[:quarter_size]
    # last_quarter = nums[-quarter_size:]
    for index in range(len(middle_part)):
        nums[index] = middle_part[index]
    for index in range(quarter_size):
        nums[len(middle_part) + index] = first_quarter[index]

def merge_lists(l1, l2):
    # TODO: implement the function to merge two lists and return merged list
    index1 = 0
    index2 = 0
    l1_length = len(l1)
    l2_length = len(l2)
    merged_list = []
    while index1 < l1_length and index2 < l2_length:
        if l1[index1] < l2[index2]:
            merged_list.append(l1[index1])
            index1 += 1
        else:
            merged_list.append(l2[index2])
            index2 += 1
    if index2 < l2_length:
        merged_list.extend(l2[index2:])
    if index1 < l1_length:
        merged_list.extend(l1[index1:])
    return merged_list

def merge_sorted_lists_descending_unique(l1, l2):
    # TODO: Implement the function
    l1_length = len(l1)
    l2_length = len(l2)
    index1 = l1_length - 1
    index2 = l2_length - 1
    merged_list = []
    while index1 >= 0 and index2 >= 0:
        item = None
        if l1[index1] > l2[index2]:
            item = l1[index1]
            index1 -= 1
        else:
            item = l2[index2]
            index2 -= 1
        if not merged_list or (merged_list and merged_list[-1] != item):
            merged_list.append(item)
    while index1 >= 0:
        item = l1[index1]
        if merged_list[-1] != item:
            merged_list.append(item)
        index1 -= 1
    while index2 >= 0:
        item = l2[index2]
        if merged_list[-1] != item:
            merged_list.append(item)
        index2 -= 1

    return merged_list


def remove_common_elements(list1, list2):
    # TODO: Implement the function here
    index1 = 0
    index2 = 0
    l1_length = len(list1)
    l2_length = len(list2)
    merged_dict = {}
    while index1 < l1_length and index2 < l2_length:
        if list1[index1] < list2[index2]:
            add_to_dict(merged_dict, list1[index1])
            index1 += 1
        else:
            add_to_dict(merged_dict, list2[index2])
            index2 += 1
    while index2 < l2_length:
        add_to_dict(merged_dict, list2[index2])
        index2 += 1
    while index1 < l1_length:
        add_to_dict(merged_dict, list1[index1])
        index1 += 1
    return [key for key, value in merged_dict.items() if value == 1]


def add_to_dict(num_dict, a_number):
    if num_dict.get(a_number) is None:
        num_dict[a_number] = 1
    else:
        num_dict[a_number] += 1

def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    # TODO: implement the function to merge sorted lists
    merged_list = []
    list_indices = {}
    total_length = 0
    for list_index, one_list in enumerate(arr):
        list_indices[list_index] = {"index": 0, "length": len(one_list)}
        total_length += len(one_list)
    while total_length > 0:
        min_value = None
        current_list = 0
        for index in list_indices.keys():
            if (list_indices[index]["index"] < list_indices[index]["length"]
            and (min_value is None or arr[index][list_indices[index]["index"]] < min_value)):
                min_value = arr[index][list_indices[index]["index"]]
                current_list = index
        merged_list.append(min_value)
        list_indices[current_list]["index"] += 1
        total_length -= 1

    return merged_list

if __name__ == "__main__":
    print(merge_n_sorted_lists([[1, 6, 10], [2, 12], [4, 7]]))