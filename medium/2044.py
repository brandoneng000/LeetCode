from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def helper(index: int, cur: int, target: int):
            if index == n:
                return 1 if cur == target else 0

            if (index, cur) in cache:
                return cache[(index, cur)]
            
            count_without = helper(index + 1, cur, target)
            count_with = helper(index + 1, cur | nums[index], target)

            cache[(index, cur)] = count_without + count_with
            return cache[(index, cur)]


        n = len(nums)
        largest = 0
        cache = {}

        for num in nums:
            largest |= num
        
        return helper(0, 0, largest)

    # def countMaxOrSubsets(self, nums: List[int]) -> int:
    #     def backtrack(cur: int, index: int):
    #         if cur == largest:
    #             self.res += 1
            
    #         for i in range(index, n):
    #             backtrack(cur | nums[i], i + 1)
        
    #     n = len(nums)
    #     largest = 0
    #     self.res = 0

    #     for num in nums:
    #         largest |= num
        
    #     backtrack(0, 0)
    #     return self.res
        
        
def main():
    sol = Solution()
    print(sol.countMaxOrSubsets([3,1]))
    print(sol.countMaxOrSubsets([2,2,2]))
    print(sol.countMaxOrSubsets([3,2,1,5]))

if __name__ == '__main__':
    main()