from typing import List
import collections

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0]
        res = 0

        for bit in nums:
            prefix.append(prefix[-1] + bit)

        count = collections.Counter()

        for val in prefix:
            res += count[val]
            count[val + goal] += 1

        return res


def main():
    sol = Solution()
    print(sol.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
    print(sol.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))

if __name__ == '__main__':
    main()