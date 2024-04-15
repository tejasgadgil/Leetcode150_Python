class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store characters and their indices
        present = dict()
        # Initialize the maximum length of the substring without repeating characters
        count = 1
        # Initialize pointers for the left and right ends of the current substring
        l, r = 0, 1
        # Get the length of the input string
        length = len(s)
        
        # If the length of the string is less than or equal to 1, return the length
        if length <= 1:
            return length
        
        # Put the first character of the string into the dictionary
        present[s[l]] = 0
        
        # Iterate through the string using the right pointer
        while r < length:
            # If the current character is already in the dictionary, update the left pointer to skip the repeating character
            if s[r] in present:
                l = max(present[s[r]] + 1, l)
            # Put the current character and its index into the dictionary
            present[s[r]] = r
            # Move the right pointer to the next character
            r += 1
            # Update the maximum length of the substring without repeating characters
            count = max(count, r - l)
        
        # Return the maximum length of the substring without repeating characters
        return count


# The time complexity is O(n), where n is the length of the input string, and the space complexity is O(min(n, m)), where m is the size of the character set.

# testcase : abcabcbb
# Itr	    present	              l	r	max
# 1	  {'a'->0, 'b'->1}	0	1	1
# 2	  {'a'->0, 'b'->1, 'c'->2}	0	2	1
# 3	  {'a'->0, 'b'->1, 'c'->2}	1	3	2
# 4	  {'a'->3, 'b'->4, 'c'->2}	1	4	2
# 5	  {'a'->3, 'b'->4, 'c'->5}	3	5	3
# 6	  {'a'->3, 'b'->6, 'c'->5}	3	6	3
# 7	  {'a'->3, 'b'->7, 'c'->5}	3	7	3
# 8	  {'a'->3, 'b'->8, 'c'->5}	3	8	3
