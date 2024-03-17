from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            cur_min = cur_max = nums[i]

            for j in range(i, n):
                cur_min = min(cur_min, nums[j])
                cur_max = max(cur_max, nums[j])
                res += cur_max - cur_min
        
        return res



def main():
    sol = Solution()
    print(sol.subArrayRanges([1,2,3]))
    print(sol.subArrayRanges([1,3,3]))
    print(sol.subArrayRanges([4,-2,-3,4,1]))

if __name__ == '__main__':
    main()