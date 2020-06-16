#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (35.73%)
# Likes:    1630
# Dislikes: 4501
# Total Accepted:    451.1K
# Total Submissions: 1.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#

'''
https://leetcode.com/problems/zigzag-conversion/discuss/3417/A-10-lines-one-pass-o(n)-time-o(1)-space-accepted-solution-with-detailed-explantation
'''

'''
https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
'''
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
        '''
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row, step = 0, 1
        for char in s:
            rows[row] += char
            row += step
            if row == numRows - 1 or row == 0:
                step *= -1
        return "".join(rows)

    def convert_2(self, s: str, numRows: int) -> str:
        '''
        https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
        '''
        if numRows == 1 or numRows >= len(s):
            return s
        result = ""
        cycle = 2 * numRows - 2
        for row in range(numRows):
            char_idx1 = row
            while char_idx1 < len(s):
                result += s[char_idx1]
                if row != 0 and row != numRows - 1:
                    char_idx2 = char_idx1 - 2 * row + cycle  # char_idx1 - row + cycle = char_idx2 + row
                    if char_idx2 < len(s):
                        result += s[char_idx2]
                char_idx1 += cycle
        return result


# @lc code=end

