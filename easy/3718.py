from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for num in range(k, k * (n + 1) + 1, k):
            if num not in nums:
                return num



def main():
    sol = Solution()
    print(sol.missingMultiple(nums = [8,2,3,4,6], k = 2))
    print(sol.missingMultiple(nums = [1,4,7,10,15], k = 5))

if __name__ == '__main__':
    main()