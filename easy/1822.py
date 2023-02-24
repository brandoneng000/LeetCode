from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        
        return 1 if not sum(num < 0 for num in nums) % 2 else -1

def main():
    sol = Solution()
    print(sol.arraySign([-1,-2,-3,-4,3,2,1]))
    print(sol.arraySign([1,5,0,2,-3]))
    print(sol.arraySign([-1,1,-1,1,-1]))

if __name__ == '__main__':
    main()