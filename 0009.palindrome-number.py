#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (43.82%)
# Likes:    2246
# Dislikes: 1536
# Total Accepted:    915.9K
# Total Submissions: 1.9M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
# @lc code=end

