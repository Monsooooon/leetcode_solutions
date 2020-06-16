#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.45%)
# Likes:    15185
# Dislikes: 550
# Total Accepted:    3M
# Total Submissions: 6.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums):
            if target - n in dic:
                return {dic[target - n], i}
            dic[n] = i

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x:x[1])
        l, r = 0, len(nums) - 1
        while l < r:
            sum = nums[l][1] + nums[r][1]
            if sum == target:
                return sorted([nums[l][0], nums[r][0]])
            elif sum < target:
                l += 1
            else:
                r -= 1
        
            

# @lc code=end

