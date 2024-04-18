class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize pointers at the start and end of the list
        l, r = 0, len(height) - 1
        # Initialize the maximum volume of water
        vol = min(height[l], height[r]) * (r - l)
        
        # Iterate until the pointers meet
        while l < r:
            # Move the pointer pointing to the smaller height towards the other pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            # Calculate the volume of water trapped between the two lines and update the maximum volume
            vol = max(vol, min(height[l], height[r]) * (r - l))

        # Return the maximum volume of water
        return vol

# The time complexity is O(n), where n is the length of the input list height.
# And the space complexity is O(1).
