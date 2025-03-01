class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        # Return the length of the palindrome
            return right-left - 1

    # Initialize start and end indices of the longest palindrome
        start, end = 0, 0

        for i in range(len(s)):
        # Case 1: Odd-length palindrome (single center)
            len1 = expand_around_center(i, i)
        # Case 2: Even-length palindrome (two centers)
            len2 = expand_around_center(i, i + 1)
        # Find the maximum length palindrome centered at i
            max_len = max(len1, len2)
        # Update start and end if a longer palindrome is found
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

    # Return the longest palindromic substring
        return s[start : end + 1]                                      
