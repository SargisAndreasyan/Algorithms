def fibo_recursive(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_recursive(num - 1) + fibo_recursive(num - 2)


if __name__ == '__main__':
    print(fibo_recursive(3))
