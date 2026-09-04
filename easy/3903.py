from typing import List

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            large = max(nums[:i + 1])
            small = min(nums[i:])

            if large - small <= k:
                return i

        return -1

def main():
    sol = Solution()
    print(sol.firstStableIndex(nums = [5,0,1,4], k = 3))
    print(sol.firstStableIndex(nums = [3,2,1], k = 1))
    print(sol.firstStableIndex(nums = [0], k = 0))

if __name__ == '__main__':
    main()