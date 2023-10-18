from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = set([0])
        res = cur = 0

        for num in nums:
            cur += num
            prev = cur - target

            if prev in seen:
                res += 1
                seen = set()
            seen.add(cur)
        
        return res

    # def maxNonOverlapping(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     prefix = [0] * (n + 1)

    #     for i in range(n):
    #         prefix[i + 1] = prefix[i] + nums[i]
        
    #     seen = { 0: 0 }
    #     res = 0

    #     for i in range(1, n + 1):
    #         cur = prefix[i]
    #         prev = cur - target

    #         if prev in seen:
    #             res += 1
    #             seen = {}

    #         seen[cur] = i
        
    #     return res


def main():
    sol = Solution()
    print(sol.maxNonOverlapping(nums = [1,1,1,1,1], target = 2))
    print(sol.maxNonOverlapping(nums = [-1,3,5,1,4,2,-9], target = 6))

if __name__ == '__main__':
    main()