class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(':')', '{':'}', '[':']'}
        stack = []
        if not s:
            return False
        
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if not char == map[last]:
                    return False
        
        return not stack  # True only if every opening bracket was matched

        