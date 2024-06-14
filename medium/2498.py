from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        res = stones[1] - stones[0]

        for i in range(2, n):
            res = max(res, stones[i] - stones[i - 2])
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxJump([0,2,5,6,7]))
    print(sol.maxJump([0,3,9]))

if __name__ == '__main__':
    main()