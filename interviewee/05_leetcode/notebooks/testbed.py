def longestPalindrome(s: str) -> str:
  n = len(s)
  dp = [[0] * n for _ in range(n)]

  # For each substring s[i...j], check if it is a palindrome. If it is,
  # then update the value of dp[i][j] to be the length of the palindrome.
  for j in range(n):
    for i in range(j + 1):
      if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1] != 0):
        dp[i][j] = j - i + 1

  # Return the longest palindromic substring by finding the maximum value
  # in the array dp and then extracting the substring from s.
  maxLength = 0
  start = 0
  end = 0
  for i in range(n):
    for j in range(n):
      if dp[i][j] > maxLength:
        maxLength = dp[i][j]
        start = i
        end = j
  return s[start:end + 1]

if __name__ == "__main__":
    s = input()
    print(longestPalindrome(s))
