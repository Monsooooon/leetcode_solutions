#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.39%)
# Likes:    4093
# Dislikes: 689
# Total Accepted:    424.8K
# Total Submissions: 1.6M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#

# @lc code=start
class Solution:
    """
    use dp since we can use previous matching results to make further decisions
    case p[i] == 'a':
    case p[i] == '.':
        use matching result from 0 to i-1
    case p[i] == '*':
        subcase 0 prev char:
            use p[0 ... i-2] to match s[0 ... j]
        subcase 1 prev char:
            use p[0 ... i-1] to match s[0 ... j]
        subcase >1 prev chars:
            use p[0 ... i] to match s[0 ... j-1] and compare prev char vs s[j]

    notice:
        * cannot be the first char of p
        ** cannot be in p
    trick:
        since we may compare p[0 ... i-2], we can add a blank space ' ' in the beginning of s & p 
    """
    def isMatch_2(self, s: str, p: str) -> bool:
        s, p = " " + s, " " + p
        len_s, len_p = len(s), len(p)
        dp = [[False] * len_p for i in range(len_s)]

        dp[0][0] = True
        for i in range(len_s):
            for j in range(1, len_p):
                if i > 0 and p[j] in (s[i], "."):  # it is only meaningful to make comparsion when s is not "empty"
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == "*":
                    dp[i][j] = (
                        dp[i][j - 2]  # zero prev char
                        or dp[i][j - 1] # one prev char
                        or (
                            i > 0
                            and p[j - 1] in (s[i], ".")
                            and dp[i - 1][j]
                        ) # multiple prev char
                    )
        return dp[-1][-1]

    def isMatch(self, s: str, p: str) -> bool:
        s, p = " " + s, " " + p
        len_s, len_p = len(s), len(p)
        dp = [False] * len_p # only works for a 1-D list, for 2-D list use deepcopy
        
        prev = dp[:]
        prev[0] = True
        for j in range(2, len_p):
            if p[j] == "*":
                prev[j] = prev[j-2]
        
        for i in range(1, len_s):
            for j in range(1, len_p):
                if i > 0 and p[j] in (s[i], "."):  # it is only meaningful to make comparsion when s is not "empty"
                    dp[j] = prev[j - 1]
                elif p[j] == "*": # j should > 1
                    dp[j] = (
                        dp[j - 2]  # zero prev char
                        or dp[j - 1] # one prev char
                        or (
                            i > 0
                            and p[j - 1] in (s[i], ".")
                            and prev[j]
                        ) # multiple prev char
                    )
            prev, dp = dp, [False] * len_p
        return prev[-1]

# @lc code=end

