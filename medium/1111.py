from typing import List

class Solution:
    # def maxDepthAfterSplit(self, seq: str) -> List[int]:
    #     res = []

    #     for i, c in enumerate(seq):
    #         if c == '(':
    #             res.append(i % 2)
    #         else:
    #             res.append(1 - i % 2)

    #     return res

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        depth = 0

        for p in seq:
            open = (p == '(')
            if open:
                depth += 1
            res.append(depth % 2)
            if not open:
                depth -= 1
        
        return res

def main():
    sol = Solution()
    print(sol.maxDepthAfterSplit("(()())"))
    print(sol.maxDepthAfterSplit("()(())()"))

if __name__ == '__main__':
    main()