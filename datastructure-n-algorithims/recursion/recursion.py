def infinity(num):
    print(f"step: {num}")
    if num == 0:
        return
    num -= 1
    infinity(num)


def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)


if __name__ == "__main__":
    infinity(3)
    print(factorial(4))
