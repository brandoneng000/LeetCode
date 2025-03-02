from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        res = [0, 0]

        for num in nums1:
            res[0] += num in nums2_set
        
        for num in nums2:
            res[1] += num in nums1_set
        
        return res


def main():
    sol = Solution()
    print(sol.findIntersectionValues(nums1 = [2,3,2], nums2 = [1,2]))
    print(sol.findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]))
    print(sol.findIntersectionValues(nums1 = [3,4,2,3], nums2 = [1,5]))

if __name__ == '__main__':
    main()