memo = 100 * [None]


def top_down_fib(n):
    """
    with top down approach we use recursive call to function
    and memorize this
    time complexity is O(2n-1)
    """
    if memo[n] is not None:
        return memo[n]

    if n in (0, 1):
        return n

    memo[n] = top_down_fib(n - 1) + top_down_fib(n - 2)
    return memo[n]


def buttom_up_fib(n):
    """
    with bottum up , this approach will use a for loop from
    small to n
    time complexity is O(n-1) better than top_down
    but it requires recalculate all state of node again
    it sounds not look like DP (spiliting and resolving)
    """
    fib_list = [0, 1]

    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[n]


if __name__ == "__main__":

    # fibonaci = [0,1,1,2,3,5,8,13]
    a = buttom_up_fib(35)
    print(a)
