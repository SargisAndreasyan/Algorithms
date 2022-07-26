from typing import List


def index_smallest(arr: List) -> int:
    smallest = arr[0]
    ind = 0
    for i, num in enumerate(arr):
        if num < smallest:
            smallest = num
            ind = i
    return ind


def selection_sort(arr: List) -> tuple:
    new_list = []
    for i in range(len(arr)):
        smallest = index_smallest(arr)
        new_list.append(arr.pop(smallest))
    return tuple(new_list)


if __name__ == '__main__':
    a = [4, 3, 7, 1, 5, 3, 1]
    print(selection_sort(a))
