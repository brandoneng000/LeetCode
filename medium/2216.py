from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if len(stack) % 2 == 0 or nums[i] != stack[-1]:
                stack.append(nums[i])
        
        if len(stack) % 2 == 1:
            stack.pop()
        
        return n - len(stack)


def main():
    sol = Solution()
    print(sol.minDeletion([1,1,2,3,5]))
    print(sol.minDeletion([1,1,2,2,3,3]))

if __name__ == '__main__':
    main()