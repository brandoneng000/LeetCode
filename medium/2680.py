from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        left = 0
        right = [0] * n

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] | nums[i + 1]
        
        for i in range(n):
            res = max(res, left | nums[i] << k | right[i])
            left |= nums[i]
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumOr(nums = [12,9], k = 1))
    print(sol.maximumOr(nums = [8,1,2], k = 2))

if __name__ == '__main__':
    main()