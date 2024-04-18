class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize a list to store the result
        res = list()
        # Sort the input list to simplify the process of finding triplets
        nums.sort()
        
        # Iterate through each element in the list
        for i, a in enumerate(nums):
            # Skip duplicates to avoid duplicate triplets
            if i != 0 and a == nums[i - 1]:
                continue
            
            # Initialize pointers for the left and right ends of the subarray
            l, r = i + 1, len(nums) - 1

            # Use two pointers to find pairs that sum up to the target
            while l < r:
                # Calculate the sum of the current triplet
                triplet_sum = nums[i] + nums[l] + nums[r]
                if triplet_sum > 0:
                    # If the sum is greater than zero, move the right pointer to decrease the sum
                    r -= 1
                elif triplet_sum < 0:
                    # If the sum is less than zero, move the left pointer to increase the sum
                    l += 1
                else:
                    # If the sum is zero, add the triplet to the result list
                    res.append([nums[i], nums[l], nums[r]])
                    # Move the left pointer to the next unique element
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        # Return the list of triplets
        return res


# The time complexity is O(n^2), where n is the length of the input array nums, and the space complexity is O(1).
