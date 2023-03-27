from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # nums1_only = set()

        # for n in nums1:
        #     if n in nums2:
        #         nums2.remove(n)
        #     else:
        #         nums1_only.add(n)

        # return [list(nums1_only), list(nums2)]
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        

def main():
    sol = Solution()
    print(sol.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
    print(sol.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))

if __name__ == '__main__':
    main()