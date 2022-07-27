from typing import List


def quick_sort(arr: List) -> List:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i <= pivot]
        great = [i for i in arr if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(great)


if __name__ == '__main__':
    print(quick_sort([5, 6, 1, 2, 8]))
