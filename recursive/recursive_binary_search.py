from typing import List


def binary_search(arr: List, high: int, low: int, num: int) -> float or int:
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            return binary_search(arr, mid - 1, low, num)
        else:
            return binary_search(arr, high, mid + 1, num)
    else:
        return -1


if __name__ == '__main__':
    arr = [i for i in range(1000)]
    arr.pop(50)
    print(binary_search(arr, len(arr), 0, 50))
