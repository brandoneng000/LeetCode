from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums = set(nums1) & set(nums2)

        if nums:
            return min(nums)
        
        x = min(nums1)
        y = min(nums2)
        return min(x, y) * 10 + max(x, y)

def main():
    sol = Solution()
    print(sol.minNumber(nums1 = [4,1,3], nums2 = [5,7]))
    print(sol.minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))

if __name__ == '__main__':
    main()