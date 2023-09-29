from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 1000000007
        horizontal = [0] + sorted(horizontalCuts) + [h]
        vertical = [0] + sorted(verticalCuts) + [w]

        height = max(horizontal[i + 1] - horizontal[i] for i in range(len(horizontal) - 1))
        width = max(vertical[i + 1] - vertical[i] for i in range(len(vertical) - 1))

        return height * width % mod
        
def main():
    sol = Solution()
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))

if __name__ == '__main__':
    main()