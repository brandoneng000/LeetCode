from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = float('inf')

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur |= nums[j]

                if cur >= k:
                    res = min(res, j - i + 1)
                    break

        return res if res != float('inf') else -1
        
def main():
    sol = Solution()
    print(sol.minimumSubarrayLength(nums = [1,2,3], k = 2))
    print(sol.minimumSubarrayLength(nums = [2,1,8], k = 10))
    print(sol.minimumSubarrayLength(nums = [1,2], k = 0))

if __name__ == '__main__':
    main()