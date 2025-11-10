from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            
            if num == 0:
                continue

            if not stack or stack[-1] < num:
                res += 1
                stack.append(num)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minOperations([0,2]))
    print(sol.minOperations([3,1,2,1]))
    print(sol.minOperations([1,2,1,2,1,2]))

if __name__ == '__main__':
    main()