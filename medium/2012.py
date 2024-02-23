from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        res = [2] * n
        res[0] = res[-1] = 0
        left = nums[0]
        right = nums[-1]

        for i in range(1, n - 1):
            left = max(left, nums[i - 1])
            if left < nums[i]:
                continue
            res[i] = 1
        
        for i in range(n - 2, 0, -1):
            right = min(right, nums[i + 1])
            if nums[i] < right and res[i] == 2:
                continue
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res[i] = 1
            else:
                res[i] = 0
        
        return sum(res)
        
def main():
    sol = Solution()
    print(sol.sumOfBeauties([1,2,3]))
    print(sol.sumOfBeauties([2,4,6,4]))
    print(sol.sumOfBeauties([3,2,1]))

if __name__ == '__main__':
    main()