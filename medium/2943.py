from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def count_consecutive(nums: List[int]):
            if not nums:
                return 0
            
            nums.sort()
            n = len(nums)
            stack = [1]

            for i in range(n - 1):
                if nums[i] + 1 == nums[i + 1]:
                    stack[-1] += 1
                else:
                    stack.append(1)

            return max(stack)

        size = min(count_consecutive(hBars), count_consecutive(vBars))

        return (1 + size) * (1 + size)
        

        
def main():
    sol = Solution()
    print(sol.maximizeSquareHoleArea(n = 6, m = 6, hBars = [2,3], vBars = [3,4]))
    print(sol.maximizeSquareHoleArea(n = 2, m = 4, hBars = [3,2], vBars = [4,2]))
    print(sol.maximizeSquareHoleArea(n = 2, m = 1, hBars = [2,3], vBars = [2]))
    print(sol.maximizeSquareHoleArea(n = 1, m = 1, hBars = [2], vBars = [2]))
    print(sol.maximizeSquareHoleArea(n = 2, m = 3, hBars = [2,3], vBars = [2,4]))

if __name__ == '__main__':
    main()