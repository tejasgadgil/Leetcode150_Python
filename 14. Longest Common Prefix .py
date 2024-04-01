class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sort the list of strings lexicographically
        strs.sort()
        
        # Get the first and last strings after sorting
        f = strs[0]
        l = strs[-1]
        
        # Determine the minimum length among the first and last strings
        n = min(len(f), len(l))
        
        # Initialize an index to track the common prefix length
        i = 0
        
        # Iterate through characters of the first and last strings until they differ or reach the minimum length
        while i < n and f[i] == l[i]:
            i += 1
        
        # Return the substring of the first string up to the common prefix length
        return f[0:i]


# Time Complexity:

# Sorting the list of strings takes O(n log n) time, where n is the number of strings in the list and the average length of the strings.
# After sorting, the algorithm iterates through characters of the first and last strings, which takes O(m) time, where m is the length of the common prefix between the first and last strings.
# Overall, the time complexity is O(n log n) due to sorting.

# Space Complexity:

# The space complexity is O(1) because the extra space used does not depend on the input size. The space usage remains constant regardless of the size of the input list or the length of the strings.
