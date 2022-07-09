def fib_fast(n,memo={}):
    if (n == 0) or (n == 1):
        return 1
    else:
        if n-1 not in memo:
            memo[n-1] = fib_fast(n-1, memo)
        if n-2 not in memo:
            memo[n-2] = fib_fast(n-1, memo)
        return memo[n-1] + memo[n-2]

print("需要fib多少数字?(int only)")
a = int(input())
print(fib_fast(a))
