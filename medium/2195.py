from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = k * (k + 1) // 2
        level = k + 1

        for num in sorted(set(nums)):
            if num < level:
                res += level - num
                level += 1
        
        return res


    # def minimalKSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     used = set(nums)
    #     res = 0

    #     for i in range(1, min(n + k, max(nums) + k) + 1):
    #         if i not in used and k:
    #             res += i
    #             k -= 1
        
    #     return res

    # def minimalKSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     unique = set(range(1, min(n + k, max(nums) + k) + 1)) - set(nums)
        
    #     return sum(sorted(unique)[:k])


        
def main():
    sol = Solution()
    print(sol.minimalKSum(nums = [1,4,25,10,25], k = 2))
    print(sol.minimalKSum(nums = [5,6], k = 6))

if __name__ == '__main__':
    main()