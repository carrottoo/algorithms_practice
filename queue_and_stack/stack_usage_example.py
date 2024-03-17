"""
    An example using stack structure to solve a problem of finding valid string parentheses

    A valid string parentheses meets the following requirements:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        current_open = [] # store current open as a stack 
        
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        for i in range(len(s)):
            if s[i] in [')',']','}']:
                if len(current_open) == 0:
                    return False
                elif s[i] == mapping[current_open[-1]]:
                    current_open.pop(-1)
                else:
                    return False
            else:
                current_open.append(s[i])
  
        if len(current_open) == 0:
            return True
        else:
            return False