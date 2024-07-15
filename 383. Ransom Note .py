class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count the occurrences of each character in the magazine
        mag = {}
        for c in magazine:
            if c in mag:
                mag[c] += 1
            else:
                mag[c] = 1

        # Check if the ransom note can be constructed with the characters in the magazine
        for c in ransomNote:
            if c in mag and mag[c] > 0:
                mag[c] -= 1  # Use one occurrence of the character
            else:
                return False  # If character not found or count is zero, return False

        return True  # If all characters in ransom note are found with sufficient counts, return True

# Time Complexity: O(n + m)
# Space Complexity: O(k)

# Approach:
# HashMap

# Time Complexity: O(n + m), where n is the length of the ransom note and m is the length of the magazine. 
# This is because we traverse both strings once.
#
# Space Complexity: O(k), where k is the number of unique characters in the magazine. 
# This is due to the storage required for the character counts in the dictionary.
