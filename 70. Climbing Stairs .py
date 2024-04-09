class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables for the first two steps of the Fibonacci sequence
        one, two = 1, 1
        
        # Iterate through the remaining steps
        for i in range(n - 1):
            # Calculate the next step by adding the two previous steps
            temp = one
            one = one + two
            two = temp
        
        # Return the number of ways to reach the top of the stairs
        return one

# This approach effectively calculates the Fibonacci sequence iteratively without the need for recursion or extra space, leading to a time complexity of O(n) and a space complexity of O(1).


        # its a fibonacci sequence bascically
        # bottom up approach
        # Eg n = 5
        #  0  1  2  3  4  5
        #  8  5  3  2  1  1
        # add -1 no : 2 steps to reach
        # add -2 no : 1 step to reach
        # eg to reach 5: 1 way is 3 (2 steps), 1 way is 4 (single step) 
