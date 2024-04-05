class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the length of the needle is greater than the length of the haystack,
        # the needle cannot be found in the haystack
        if len(needle) > len(haystack):
            return -1

        l = 0
        # Iterate through the haystack until the remaining length is enough to accommodate the needle
        while l < len(haystack) - len(needle) + 1:
            r = l
            # If the current character in the haystack matches the first character of the needle
            if haystack[r] == needle[0]:
                i = 0
                # Compare subsequent characters of the haystack and needle until the needle is fully matched or there's a mismatch
                while i < len(needle) and r < len(haystack) and haystack[r] == needle[i]:
                    i += 1
                    r += 1
                # If all characters of the needle are matched, return the starting index of the match
                if i == len(needle):
                    return r - i
            l += 1

        # If the needle is not found in the haystack, return -1
        return -1

# Time Complexity:
# The time complexity of this solution is O((n - m) * m), where n is the length of the haystack and m is the length of the needle. This is because the algorithm iterates through each possible starting position of the needle in the haystack, and for each starting position, it compares at most m characters.

# Space Complexity:
# The space complexity is O(1) because the extra space used does not depend on the size of the input. The algorithm uses only a constant amount of extra space for pointers and variables.
