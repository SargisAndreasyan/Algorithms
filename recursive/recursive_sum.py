from typing import List


def recursive_sum(arr: List) -> float or int:
    if len(arr) != 1:
        return arr[0] + recursive_sum(arr[1:])
    else:
        return arr[0]
