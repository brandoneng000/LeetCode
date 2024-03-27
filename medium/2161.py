from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = []
        right = []
        pivot_count = 0

        for i in range(n):
            if nums[i] == pivot:
                pivot_count += 1
            elif nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        
        return left + [pivot] * pivot_count + right

        
def main():
    sol = Solution()
    print(sol.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))
    print(sol.pivotArray(nums = [-3,4,3,2], pivot = 2))

if __name__ == '__main__':
    main()