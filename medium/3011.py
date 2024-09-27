from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        stack = [[]]
        bits = nums[0].bit_count()

        for num in nums:
            if bits == num.bit_count():
                stack[-1].append(num)
            else:
                bits = num.bit_count()
                stack.append([num])
            
        for i in range(len(stack) - 1):
            if max(stack[i]) > min(stack[i + 1]):
                return False

        return True
        
def main():
    sol = Solution()
    print(sol.canSortArray(nums = [8,4,2,30,15]))
    print(sol.canSortArray(nums = [1,2,3,4,5]))
    print(sol.canSortArray(nums = [3,16,8,4,2]))

if __name__ == '__main__':
    main()