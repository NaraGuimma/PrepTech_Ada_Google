# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = {}
        i = 0
        while i < len(nums):
            if i == (len(nums) - 1):
                count[nums[i]] = i + 1
                break
            if nums[i] != nums[i+1]:
                count[nums[i]] = i + 1
                nums = list(filter(lambda a: a != nums[i], nums))
                i = 0
            else:
                 i += 1
        v = list(count.values())
        k = list(count.keys())
        return k[v.index(max(v))]
