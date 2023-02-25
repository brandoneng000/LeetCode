from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = float('inf')

        for index, val in enumerate(nums):
            if target == val:
                result = min(result, abs(index - start))
        
        return result

def main():
    sol = Solution()
    print(sol.getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3))
    print(sol.getMinDistance(nums = [1], target = 1, start = 0))
    print(sol.getMinDistance(nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0))

if __name__ == '__main__':
    main()