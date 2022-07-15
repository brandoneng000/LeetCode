class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if not stack:
                    return False
                elif p == ")" and stack[-1] == "(" or \
                     p == "]" and stack[-1] == "[" or \
                     p == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        return not stack
                
        
def main():
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))
    print(sol.isValid("{"))

if __name__ == '__main__':
    main()