# 678. Valid Parenthesis String (M)
"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        stk=[]
        for chr in s:
            if chr=='(':
                stk.append(')')
            if chr==')':
                if stk:
                    stk.pop()
        return len(stk)==0

sl = Solution()
# print(sl.checkValidString("(*))"))  # True
# print(sl.checkValidString("(*)"))    # True
# print(sl.checkValidString("(*)("))   # False
print(sl.checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()"))   # False

