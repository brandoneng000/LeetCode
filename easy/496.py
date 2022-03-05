from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack = []
        greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)

        for index, num in enumerate(nums1):
            result[index] = greater[num] if num in greater else -1

        return result
        
def main():
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(sol.nextGreaterElement([2,4], [1,2,3,4]))

if __name__ == '__main__':
    main()