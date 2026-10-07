from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def forward(s: str, res: str, li: int, lj: int):
            n = len(s)
            bal = 0

            for i in range(li, n):
                bal += (s[i] == '(') - (s[i] == ')')

                if bal >= 0:
                    continue

                for j in range(lj, i + 1):
                    if s[j] == ')' and (j == lj or s[j - 1] != ')'):
                        next_s = s[:j] + s[j + 1:]
                        forward(next_s, res, i, j)

                return

            backward(s, res, n - 1, n - 1)

        def backward(s: str, res: str, ri: int, rj: int):
            bal = 0

            for i in range(ri, -1, - 1):
                bal += (s[i] == ')') - (s[i] == '(')

                if bal >= 0:
                    continue

                for j in range(rj, i - 1, -1):
                    if s[j] == '(' and (j == rj or s[j + 1] != '('):
                        next_s = s[:j] + s[j + 1:]
                        backward(next_s, res, i - 1, j - 1)

                return

            res.append(s)

        res = []
        forward(s, res, 0, 0)
        return res

def main():
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
    print(sol.removeInvalidParentheses("(a)())()"))
    print(sol.removeInvalidParentheses(s = ")("))

if __name__ == '__main__':
    main()