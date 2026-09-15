
def fibonacci_memo(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci_memo(n - 1, dp) + fibonacci_memo(n - 2, dp)
    return dp[n]


# Tabulation (Bottom-Up)
def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter the value of n: "))

dp = [-1] * (n + 1)
memo_result = fibonacci_memo(n, dp)

tab_result = fibonacci_tab(n)

print("\nUsing Memoization :", memo_result)
print("Using Tabulation  :", tab_result)