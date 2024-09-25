from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        combine_set = len(nums1_set & nums2_set)
        nums1_diff = len(nums1_set - nums2_set)
        nums2_diff = len(nums2_set - nums1_set)
        res = 0

        if m // 2 > nums1_diff:
            res += nums1_diff
            res += min(m // 2 - nums1_diff, combine_set)
            combine_set = max(0, combine_set - (m // 2 - nums1_diff))
        else:
            res += min(m // 2, nums1_diff)
        
        if n // 2 > nums2_diff:
            res += nums2_diff
            res += min(n // 2 - nums2_diff, combine_set)
        else:
            res += min(n // 2, nums2_diff)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumSetSize(nums1 = [1,1,1,1], nums2 = [12,23,41,9]))
    print(sol.maximumSetSize(nums1 = [1,2,1,2], nums2 = [1,1,1,1]))
    print(sol.maximumSetSize(nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]))
    print(sol.maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))

if __name__ == '__main__':
    main()