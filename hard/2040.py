from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helper(nums2: List[int], x1: int, v: int):
            if x1 > 0:
                return bisect_right(nums2, v // x1)
            elif x1 < 0:
                return len(nums2) - bisect_left(nums2, -(-v // x1))
            else:
                return len(nums2) if v >= 0 else 0
        
        n1 = len(nums1)
        left = -(10 ** 10)
        right = 10 ** 10

        while left <= right:
            middle = (left + right) // 2
            count = 0

            for i in range(n1):
                count += helper(nums2, nums1[i], middle)
            
            if count < k:
                left = middle + 1
            else:
                right = middle - 1
        
        return left

        
def main():
    sol = Solution()
    print(sol.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))
    print(sol.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
    print(sol.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))

if __name__ == '__main__':
    main()