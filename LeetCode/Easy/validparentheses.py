# Solution to Problem "Valid Parentheses" on LeetCode
# A. K. Nguyen
# Boston University 2022

def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Runtime: 15ms
        Memory: 13.5 MB
        """
        stack = []
        
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                current_char = stack.pop()
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False

        if len(stack) != 0:
            return False
        return True

print(isValid("{}()"))
print(isValid("{}[}()"))
print(isValid("{()}"))
