from typing import List

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses = []
        pair = [0] * n

        for i in range(n):
            if s[i] == '(':
                open_parentheses.append(i)
            if s[i] == ')':
                j = open_parentheses.pop()
                pair[i] = j
                pair[j] = i

        res = []
        idx = 0
        direction = 1

        while idx < n:
            if s[idx] == '(' or s[idx] == ')':
                idx = pair[idx]
                direction = -direction
            else:
                res.append(s[idx])
            idx += direction

        return "".join(res)

    # def reverseParentheses(self, s: str) -> str:
    #     stack = []

    #     for c in s:
    #         if c == ')':
    #             temp = []
    #             while stack[-1] != '(':
    #                 temp.append(stack.pop())
    #             stack.pop()
    #             stack.extend(temp)
    #         else:
    #             stack.append(c)
        
    #     return "".join(stack)

def main():
    sol = Solution()
    print(sol.reverseParentheses("(abcd)"))
    print(sol.reverseParentheses("(u(love)i)"))
    print(sol.reverseParentheses("(ed(et(oc))el)"))

if __name__ == '__main__':
    main()