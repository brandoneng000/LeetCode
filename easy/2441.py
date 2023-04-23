from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        found = set()
        matching = set()
        for num in nums:
            if num in found:
                matching.add(abs(num))
            found.add(-num)
        
        return max(matching) if matching else -1

def main():
    sol = Solution()
    print(sol.findMaxK([-1,2,-3,3]))
    print(sol.findMaxK([-1,10,6,7,-7,1]))
    print(sol.findMaxK([-10,8,6,7,-2,-3]))

if __name__ == '__main__':
    main()