# 09-02-2025
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack
      
# Explanation : 
# 1.Use a stack to keep track of opening brackets.
# 2.A dictionary mapping is used to map closing brackets to their corresponding opening brackets.
# 3.Loop Through String: For each character,If it's an opening bracket push it onto the stack.
# If it's a closing bracket, check if it matches the top of the stack (pop from stack). If not, return False.
# Final Check: If the stack is empty at the end, return True (all brackets are matched). Otherwise, return False.
# This efficiently checks if parentheses in the string are properly balanced.
