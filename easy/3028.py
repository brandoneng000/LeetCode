from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        cur = 0

        for num in nums:
            cur += num
            res += cur == 0
        
        return res
        
def main():
    sol = Solution()
    print(sol.returnToBoundaryCount([2,3,-5]))
    print(sol.returnToBoundaryCount([3,2,-3,-4]))

if __name__ == '__main__':
    main()