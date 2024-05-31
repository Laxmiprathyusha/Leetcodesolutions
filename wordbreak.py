def word_break(s, wordDict):
    word_set = set(wordDict)  # Convert the wordDict to a set for O(1) lookups
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Empty string is considered segmented

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further if dp[i] is True

    return dp[len(s)]

# Example usage:
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(word_break(s1, wordDict1))  # Output: True

s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print(word_break(s2, wordDict2))  # Output: True

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(word_break(s3, wordDict3))  # Output: False
