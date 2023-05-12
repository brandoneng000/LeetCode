from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        val = -float('inf')
        for n in nums[::-1]:
            if n < val:
                return True
            while stack and stack[-1] < n:
                val = stack.pop()
            stack.append(n)
        
        return False
        

def main():
    sol = Solution()
    print(sol.find132pattern([1,4,0,-1,-2,-3,-1,-2]))
    print(sol.find132pattern([-2,1,2,-2,1,2]))
    print(sol.find132pattern([1,2,3,4]))
    print(sol.find132pattern([3,1,4,2]))
    print(sol.find132pattern([-1,3,2,0]))

if __name__ == '__main__':
    main()