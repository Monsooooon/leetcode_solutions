#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.73%)
# Likes:    3305
# Dislikes: 5223
# Total Accepted:    1.1M
# Total Submissions: 4.2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        pos_inf, neg_inf = 2**31 - 1, -(2**31)
        if x == neg_inf:
            return 0
        if x < 0:
            return -1 * Solution().reverse(-x)
        result = 0
        while x:
            if result > pos_inf // 10: # detect overflow: result * 10 > pos_inf ?
                return 0
            result *= 10
            if result > pos_inf - x % 10: # detect overflow result + x % 10 > pos_inf ?
                return 0
            result += x % 10
            x //= 10
        return result
# @lc code=end

