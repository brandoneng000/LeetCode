from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # cache = {}
        
        # def recursive(cur: List[int]) -> int:
        #     if sum(cur) == target:
        #         return 1
        #     elif sum(cur) > target:
        #         return 0

        #     found = 0
        #     if sum(cur) not in cache:
        #         for num in nums:
        #             total = num + sum(cur)
        #             if total < target:
        #                 cur.append(num)
        #                 found += recursive(cur)
        #                 cur.pop()
        #             elif total == target:
        #                 found += 1
        #         cache[sum(cur)] = found
        #         return found
        #     else:
        #         return cache[sum(cur)]

        # return recursive([])
        cache = { 0: 1 }

        for total in range(1, target + 1):
            cache[total] = 0
            for n in nums:
                cache[total] += cache.get(total - n, 0)

        return cache[target]

def main():
    sol = Solution()
    print(sol.combinationSum4(nums = [1,2,3], target = 4))
    print(sol.combinationSum4(nums = [1,2,5,3], target = 4))
    print(sol.combinationSum4(nums = [9], target = 3))
    print(sol.combinationSum4(nums = [4,2,1], target = 32))

if __name__ == '__main__':
    main()