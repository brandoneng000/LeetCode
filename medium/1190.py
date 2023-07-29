from typing import List

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
        
        return "".join(stack)

def main():
    sol = Solution()
    print(sol.reverseParentheses("(abcd)"))
    print(sol.reverseParentheses("(u(love)i)"))
    print(sol.reverseParentheses("(ed(et(oc))el)"))

if __name__ == '__main__':
    main()