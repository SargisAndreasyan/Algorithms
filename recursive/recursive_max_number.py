from typing import List


def recursive_biggest(arr: List) -> float or int:
    if len(arr) != 1:
        return arr[0] if arr[0] > recursive_biggest(arr[1:]) else recursive_biggest(arr[1:])
    else:
        return arr[0]

if __name__ == '__main__':
    print(recursive_biggest([1,2,4,1]))