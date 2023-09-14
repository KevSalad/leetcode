# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Brute Force Solution

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        curr_max = 1
        i = 0

        # Sort the array
        nums = list(set(nums))
        nums.sort()

        # Check if the next element is consecutive, go til the end of the array
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] == 1:
                curr_max += 1
            else:
                curr_max = 1 # Reset the current max
            i += 1
            # Finally check if the curr_max length is greater than the max_length
            if curr_max > max_length:
                max_length = curr_max

        return max_length
    
'''

# Time Complexity: O(nlogn)

# Hashmap Solution
