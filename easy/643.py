from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        largest_total = total

        for index in range(k, len(nums)):
            total = total - nums[index - k] + nums[index]
            largest_total = max(total, largest_total)

        return largest_total / k

def main():
    sol = Solution()
    print(sol.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
    print(sol.findMaxAverage(nums = [5], k = 1))
    print(sol.findMaxAverage(nums = [0,1,1,3,3], k = 4))

if __name__ == '__main__':
    main()