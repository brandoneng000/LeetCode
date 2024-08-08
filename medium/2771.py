from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = dp1 = dp2 = 1

        for i in range(1, n):
            cur11 = dp1 + 1 if nums1[i - 1] <= nums1[i] else 1
            cur12 = dp1 + 1 if nums1[i - 1] <= nums2[i] else 1
            cur21 = dp2 + 1 if nums2[i - 1] <= nums1[i] else 1
            cur22 = dp2 + 1 if nums2[i - 1] <= nums2[i] else 1

            dp1 = max(cur11, cur21)
            dp2 = max(cur12, cur22)

            res = max(res, dp1, dp2)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxNonDecreasingLength(nums1 = [2,3,1], nums2 = [1,2,1]))
    print(sol.maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4]))
    print(sol.maxNonDecreasingLength(nums1 = [1,1], nums2 = [2,2]))

if __name__ == '__main__':
    main()