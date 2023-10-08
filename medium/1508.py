from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 1000000007
        all_nums = []

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                all_nums.append(cur)
        
        all_nums.sort()
        return sum(all_nums[left - 1: right]) % mod

        
def main():
    sol = Solution()
    print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
    print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
    print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))

if __name__ == '__main__':
    main()