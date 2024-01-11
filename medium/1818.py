from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 1000000007
        sorted_nums1 = sorted(nums1)
        n = len(sorted_nums1)
        res = max_reduce = 0

        for i, val in enumerate(nums2):
            cur_diff = abs(nums1[i] - val)
            res += cur_diff
            j = bisect.bisect_right(sorted_nums1, val) - 1
            op1 = abs(val - sorted_nums1[j])
            op2 = None

            if j + 1 < n:
                op2 = abs(val - sorted_nums1[j + 1])
            
            max_reduce = max(cur_diff - op1, cur_diff - op2 if op2 else 0, max_reduce)
        
        return (res - max_reduce) % mod

        
def main():
    sol = Solution()
    print(sol.minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))
    print(sol.minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]))
    print(sol.minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))

if __name__ == '__main__':
    main()