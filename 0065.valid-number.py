#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (14.12%)
# Likes:    711
# Dislikes: 4700
# Total Accepted:    166.7K
# Total Submissions: 1.1M
# Testcase Example:  '"0"'
#
# Validate if a given string can be interpreted as a decimal number.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one. However, here is a
# list of characters that can be in a valid decimal number:
# 
# 
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# 
# 
# Of course, the context of these characters also matters in the input.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
# 
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        Test cases (->False):
        e, ee, 1e, .e1, +1e, 1e.1, 1.e.1, 1.1.e
        Test cases (->True):
        +1e1, 1e1, 1.e1, .1e1, +1e+1
        '''
        # delete leading and trailing spaces
        s = s.strip()
        if not s:
            return False

        # control flags
        dot_seen = False
        e_seen = False
        digit_seen_before_e = False
        digit_seen_after_e = False

        for i in range(len(s)):
            x = s[i]
            if '0' <= x and x <= '9':
                if not e_seen:
                    digit_seen_before_e = True
                else:
                    digit_seen_after_e = True
            elif x == '+' or  x == '-':
                # "1e+1" or "1+e" -> False
                if i > 0 and s[i-1] != 'e':
                    return False
            elif x == '.':
                # "1e.1" or "1.1." -> False
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif x == 'e':
                # ".e1" or "+.e1" -> False, "1.e1" -> True
                if e_seen or not digit_seen_before_e: 
                    return False
                e_seen = True
            else:
                return False
        
        # "e1", "1e.", "1e+" -> False
        return digit_seen_before_e and (not e_seen or digit_seen_after_e)

        
# @lc code=end

