from typing import List
from collections import Counter

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count = Counter()

        for num in nums:
            count[num % space] += 1

        max_destroy = max(count.values())

        return min(i for i in set(nums) if count[i % space] == max_destroy)

        
        
    # def destroyTargets(self, nums: List[int], space: int) -> int:
    #     count = Counter(nums)
    #     sorted_count = sorted(count)
    #     n = len(sorted_count)
    #     visited = set()
    #     res = min(count)
    #     max_destroy = 0

    #     for i in range(n):
    #         if sorted_count[i] in visited:
    #             continue

    #         visited.add(sorted_count[i])
    #         cur = count[sorted_count[i]]
    #         for j in range(i + 1, n):
    #             if (sorted_count[j] - sorted_count[i]) % space == 0:
    #                 visited.add(sorted_count[j])
    #                 cur += count[sorted_count[j]]

    #         if cur > max_destroy:
    #             max_destroy = cur
    #             res = sorted_count[i]
        
    #     return res

def main():
    sol = Solution()
    print(sol.destroyTargets(nums = [3,7,8,1,1,5], space = 2))
    print(sol.destroyTargets(nums = [1,3,5,2,4,6], space = 2))
    print(sol.destroyTargets(nums = [6,2,5], space = 100))

if __name__ == '__main__':
    main()