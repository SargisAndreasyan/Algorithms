from typing import List


def recursive_count(arr: List) -> float or int:
    if len(arr) != 1:
        return 1 + recursive_count(arr[1:])
    else:
        return 1


if __name__ == '__main__':
    print(recursive_count([1, 2, 3]))
