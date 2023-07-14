from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}

        def helper(index1: int, index2: int):
            if index1 <= 0 or index2 <= 0:
                return 0
            
            if (index1, index2) in cache:
                return cache[(index1, index2)]
            
            if nums1[index1 - 1] == nums2[index2 - 1]:
                cache[(index1, index2)] = 1 + helper(index1 - 1, index2 - 1)
            else:
                cache[(index1, index2)] = max(helper(index1 - 1, index2), helper(index1, index2 - 1))
            return cache[(index1, index2)]

        return helper(len(nums1), len(nums2))

    # def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    #     def lcs(index1: int, index2: int):
    #         if index1 == 0 or index2 == 0:
    #             return 0
    #         elif nums1[index1 - 1] == nums2[index2 - 1]:
    #             return 1 + lcs(index1 - 1, index2 - 1)
    #         else:
    #             return max(lcs(index1 - 1, index2), lcs(index1, index2 - 1))

    #     return lcs(len(nums1), len(nums2))

def main():
    sol = Solution()
    print(sol.maxUncrossedLines(nums1 = [3,3], nums2 = [1,3,1,2,1]))
    print(sol.maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4]))
    print(sol.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
    print(sol.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]))

if __name__ == '__main__':
    main()