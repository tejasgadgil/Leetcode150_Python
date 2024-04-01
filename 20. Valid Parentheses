class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to store opening brackets
        stack = list()
        # Dictionary to map closing brackets to their corresponding opening brackets
        brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        # Iterate through each character in the input string
        for i in s:
            if i in '({[':  # If the character is an opening bracket
                stack.append(i)
            elif len(stack) != 0 and stack[-1] == brackets[i]:  # If the character is a closing bracket
                stack.pop()
            else:  # If the character is a closing bracket, but stack is empty or the top of stack doesn't match
                return False
        # If all opening brackets have been matched and stack is empty, return True, otherwise return False
        return len(stack) == 0

# Time Complexity:
# The time complexity of this solution is O(n), where n is the length of the input string 's'. This is because the algorithm iterates through each character of the string once.

# Space Complexity:
# The space complexity is O(n), where n is the length of the input string 's'. This is because the algorithm uses a stack to store opening brackets, and in the worst case, the stack could contain all the opening brackets if the string consists entirely of opening brackets.
