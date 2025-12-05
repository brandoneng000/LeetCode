from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = 0
        right = sum(nums)

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            res += (left - right) % 2 == 0
        
        return res
        
def main():
    sol = Solution()
    print(sol.countPartitions([10,10,3,7,6]))
    print(sol.countPartitions([1,2,2]))
    print(sol.countPartitions([2,4,6,8]))

if __name__ == '__main__':
    main()