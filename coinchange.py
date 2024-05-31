def coinChange(coins, amount):
    # Initialize the DP array with amount + 1 (a value greater than any possible answer)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: no coins needed to make 0 amount

    # Loop through all amounts from 1 to amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still amount + 1, it means we couldn't form the amount
    return dp[amount] if dp[amount] != amount + 1 else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3
