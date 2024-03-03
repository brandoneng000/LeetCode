from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(cur: int, index: int):
            if cur == largest:
                self.res += 1
            
            for i in range(index, n):
                backtrack(cur | nums[i], i + 1)
        
        n = len(nums)
        largest = 0
        self.res = 0

        for num in nums:
            largest |= num
        
        backtrack(0, 0)
        return self.res
        
        
def main():
    sol = Solution()
    print(sol.countMaxOrSubsets([3,1]))
    print(sol.countMaxOrSubsets([2,2,2]))
    print(sol.countMaxOrSubsets([3,2,1,5]))

if __name__ == '__main__':
    main()