from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        res = float('inf')

        for i in range(n // 2):
            res = min(res, (nums[i] + nums[n - i - 1]) / 2)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumAverage([7,8,3,4,15,13,4,1]))
    print(sol.minimumAverage([1,9,8,3,10,5]))
    print(sol.minimumAverage([1,2,3,7,8,9]))

if __name__ == '__main__':
    main()