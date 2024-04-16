class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Initialize variables to store the longest palindrome substring and its length
        res = ''
        reslen = 0
        n = len(s)

        # Iterate through each character in the string
        for i in range(n):
            # Odd-length palindromes: expand around the current character
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                # Update the longest palindrome substring if a longer one is found
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    res = s[l:r + 1]
                # Expand the window
                l -= 1
                r += 1

            # Even-length palindromes: expand around the current and next characters
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                # Update the longest palindrome substring if a longer one is found
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    res = s[l:r + 1]
                # Expand the window
                l -= 1
                r += 1

        # Return the longest palindrome substring found
        return res

# The time complexity is O(n^2), where n is the length of the input string, and the space complexity is O(1).
