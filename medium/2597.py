from typing import List
from collections import Counter

class Solution:        
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(num: int, g: dict):
            if num not in g:
                return 1
            if num in cache:
                return cache[num]

            skip = helper(num + k, g)
            count = g[num]
            include = (2 ** count - 1) * helper(num + 2 * k, g)
            cache[num] = skip + include
            return cache[num]

        count = Counter(nums)
        groups = []
        visited = set()
        cache = {}
        res = 1
        

        for num in count.keys():
            if num in visited:
                continue
            g = {}
            
            while num - k in count:
                num -= k
            while num in count:
                g[num] = count[num]
                visited.add(num)
                num += k

            groups.append(g)
        
        for g in groups:
            num = min(g.keys())
            res *= helper(num, g)

        return res - 1

    # def beautifulSubsets(self, nums: List[int], k: int) -> int:
    #     def helper(index: int, count: Counter):
    #         if index == n:
    #             return 1
            
    #         res = helper(index + 1, count)
    #         if not count[nums[index] + k] and not count[nums[index] - k]:
    #             count[nums[index]] += 1
    #             res += helper(index + 1, count)
    #             count[nums[index]] -= 1

    #         return res
        
    #     n = len(nums)
    #     return helper(0, Counter()) - 1

        
def main():
    sol = Solution()
    print(sol.beautifulSubsets(nums = [2,4,6], k = 2))
    print(sol.beautifulSubsets(nums = [1], k = 1))

if __name__ == '__main__':
    main()