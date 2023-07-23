from typing import List

class Solution:
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