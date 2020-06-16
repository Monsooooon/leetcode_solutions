#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (30.12%)
# Likes:    9121
# Dislikes: 554
# Total Accepted:    1.5M
# Total Submissions: 5.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_pos = max_len = 0
        used_char = {}
        for i, char in enumerate(s):
            # if we see the char in the first time, or we have seen it before, 
            # but its previos index is not in the crurrent string range
            if char not in used_char or used_char[char] < start_pos:
                max_len = max(max_len, i - start_pos + 1)
            else:
                start_pos = used_char[char] + 1
            used_char[char] = i
        return max_len

# @lc code=end

