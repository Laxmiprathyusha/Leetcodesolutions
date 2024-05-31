def climb_stairs(n):
    if n == 1:
        return 1
    
    # Initialize an array to store the number of distinct ways for each step
    dp = [0] * (n + 1)
    
    # There is only one way to climb to the first step
    dp[1] = 1
    # There are two ways to climb to the second step (1 step + 1 step, or 2 steps)
    dp[2] = 2
    
    # Calculate the number of distinct ways for each step starting from the third step
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Example usage:
n = 2
print(climb_stairs(n))  # Output: 2
