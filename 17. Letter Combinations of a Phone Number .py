class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define the mapping of each digit to its corresponding letters
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz' 
        }
        # Initialize a list to store the result
        result = []

        # Define a backtracking function to generate all possible letter combinations
        def backtrack(i, currentstr):
            # Base case: If the length of the current combination equals the length of the input digits, add it to the result
            if len(currentstr) == len(digits):
                result.append(currentstr)
                return
            # For each letter corresponding to the current digit, recursively call the backtrack function
            for l in letters[digits[i]]:
                backtrack(i + 1, currentstr + l)
            
        # If the input string is not empty, start the backtracking process
        if digits:
            backtrack(0, '')
        
        # Return the list of all possible letter combinations
        return result

# This solution effectively generates all possible letter combinations using backtracking. 
# The time complexity is exponential, as there can be up to 4^n combinations in the worst case (where n is the length of the input string of digits). 
# The space complexity is also exponential due to the recursion stack.
