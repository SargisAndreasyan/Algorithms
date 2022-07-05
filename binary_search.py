from typing import List


def binary_search(my_lst: List[int or float], item: int or float) -> int or None:
    # Low and high borders of list
    low = 0
    high = len(my_lst) - 1
    # Repeat until len our list equal 1
    while high >= low:
        # print('repeat')
        mid = (high + low) // 2
        guess = my_lst[mid]
        # if we found number
        if item == guess:
            return mid
        # Change borders
        if item < guess:
            high = mid - 1
        else:
            low = mid + 1
    # Return None if number not found
    return None


if __name__ == '__main__':
    a_lst = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search(a_lst, 6))
