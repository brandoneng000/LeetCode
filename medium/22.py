from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def tree(para: List[str], left: int, right: int):
            if len(para) == 2 * n:
                res.append("".join(para))
                return
            if left < n:
                para.append("(")
                tree(para, left + 1, right)
                para.pop()
            if right < left:
                para.append(")")
                tree(para, left, right + 1)
                para.pop()
        
        tree([], 0, 0)

        return res

def main():
    sol = Solution()
    print(sol.generateParenthesis(3))

if __name__ == '__main__':
    main()