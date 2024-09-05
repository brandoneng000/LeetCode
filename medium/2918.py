from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        total1 = sum(nums1) + zeros1
        total2 = sum(nums2) + zeros2

        if total1 > total2 and zeros2 == 0:
            return -1
        
        if total1 < total2 and zeros1 == 0:
            return -1

        return max(total1, total2)


        
def main():
    sol = Solution()
    print(sol.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))
    print(sol.minSum(nums1 = [2,0,2,0], nums2 = [1,4]))

if __name__ == '__main__':
    main()