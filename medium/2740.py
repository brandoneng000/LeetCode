from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return min(nums[i + 1] - nums[i] for i in range(n - 1))
        
def main():
    sol = Solution()
    print(sol.findValueOfPartition([1,3,2,4]))
    print(sol.findValueOfPartition([100,1,10]))

if __name__ == '__main__':
    main()