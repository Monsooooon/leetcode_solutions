#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.23%)
# Likes:    6653
# Dislikes: 525
# Total Accepted:    919.9K
# Total Submissions: 3.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        i = 0
        while i < len(s):
            l, r = i, i
            while r < len(s) and s[i] == s[r]:
                r += 1
            i = r  # s[i...r-1] contains the same char, therefore update i
            r -= 1 # r-1 is the right side of the palindrome, so decrease r
            # start expanding from l and r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if (len(longest)) < r - l - 1:
                longest = s[l + 1 : r]
        return longest


# @lc code=end
