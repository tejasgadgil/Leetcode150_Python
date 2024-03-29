class Solution:
    def romanToInt(self, s: str) -> int:
        # Replace special substrings with simpler equivalents to simplify processing
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        
        # Initialize result variable to accumulate the total integer value
        result = 0
        
        # Dictionary to map Roman numeral characters to their corresponding integer values
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Iterate through each character in the simplified Roman numeral string
        for num in s:
            # Add the integer value corresponding to the current character to the result
            result += value[num]
        
        # Return the final accumulated result
        return result



# Time Complexity:
# The time complexity of this solution is O(n), where n is the length of the input string 's'. This is because the algorithm iterates through each character of the string once to compute the integer value.

# Space Complexity:
# The space complexity is O(1) because the extra space used does not grow with the size of the input. The dictionary value contains a fixed number of mappings for Roman numeral characters to their integer values, which remains constant regardless of the input size.
