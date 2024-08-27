from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            cur = v = heights[i]

            for j in range(i - 1, -1, -1):
                v = min(v, heights[j])
                cur += v

            v = heights[i]
            for j in range(i + 1, n):
                v = min(v, heights[j])
                cur += v
            
            res = max(res, cur)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumSumOfHeights([5,3,4,1,1]))
    print(sol.maximumSumOfHeights([6,5,3,9,2,7]))
    print(sol.maximumSumOfHeights([3,2,5,5,2,3]))

if __name__ == '__main__':
    main()