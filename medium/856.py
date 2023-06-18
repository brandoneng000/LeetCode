class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for p in s:
            if p == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
            
        return stack.pop()
    # def scoreOfParentheses(self, s: str) -> int:
    #     addition = False
    #     mult = []
    #     stack = []
    #     res = cur = 0

    #     for p in s:
    #         if p == '(' and not addition:
    #             addition = True
    #         elif p == '(' and addition:
    #             mult.append(True)
    #             stack.append(cur)
    #             cur = 0
    #         elif p == ')' and addition:
    #             addition = False
    #             cur += 1
    #         elif p == ')' and not addition:
    #             mult.pop()
    #             cur *= 2
    #             cur += stack.pop()
            
    #         if not addition and not mult:
    #             res += cur
    #             cur = 0

    #     return res

def main():
    sol = Solution()
    print(sol.scoreOfParentheses("(()(()))"))
    print(sol.scoreOfParentheses("()"))
    print(sol.scoreOfParentheses("(())"))
    print(sol.scoreOfParentheses("()()"))

if __name__ == '__main__':
    main()