from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = 0
        cur = 0

        for num in nums:
            res += cur
            cur = max(cur, num)
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.findMaximumScore([1,3,1,5]))
    print(sol.findMaximumScore([4,3,1,3,2]))

if __name__ == '__main__':
    main()