def insertion_sort(arr):
    # TODO: implement the Insertion Sort algorithm
    array_length = len(arr)
    index = 1
    while index < array_length:
        current_index = index
        while current_index > 0:
            if arr[current_index] < arr[current_index - 1]:
                arr[current_index], arr[current_index - 1] = arr[current_index - 1], arr[current_index]
            elif arr[current_index] >= arr[index - 1]:
                break
            current_index -= 1
        index += 1
    return arr

def merge_sort(lst):
    # TODO: Implement the merge sort algorithm
    if lst is not None and len(lst) > 1:
        split_index = int(len(lst) / 2)
        first_half = merge_sort(lst[:split_index])
        second_half = merge_sort(lst[split_index:])
        return merge_lists(second_half, first_half)
    else:
        return lst

def merge_lists(l1, l2):
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

def quicksort_custom(arr):
    # TODO: implement the QuickSort algorithm here
    if arr is None or len(arr) <= 1:
        return arr
    pivot_number = arr[int(len(arr) / 2)]
    less_portion = []
    greater_portion = []
    equal_portion = []
    for a_number in arr:
        if a_number < pivot_number:
            less_portion.append(a_number)
        elif a_number > pivot_number:
            greater_portion.append(a_number)
        else:
            equal_portion.append(a_number)
    return quicksort_custom(less_portion) + equal_portion + quicksort_custom(greater_portion)

if __name__ == "__main__":
    print(merge_sort([2, 1, 7, 3, 4, 5]))
    print(insertion_sort([2, 1, 7, 3, 4, 5]))