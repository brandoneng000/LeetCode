from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1 for i in range(n)]
        nums.sort()
        index = 0
        
        for i in range(0, n, 2):
            res[i] = nums[index]
            index += 1
        
        for i in range(1, n, 2):
            res[i] = nums[index]
            index += 1
        
        return res



def main():
    sol = Solution()
    print(sol.rearrangeArray([1,2,3,4,5]))
    print(sol.rearrangeArray([6,2,0,9,7]))

if __name__ == '__main__':
    main()