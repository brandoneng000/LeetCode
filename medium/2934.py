from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1: List[int], nums2: List[int]):
            n = len(nums1)
            res = 0

            for i in range(n):
                if nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                    continue
                elif nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
                    res += 1
                else:
                    return float('inf')
            
            return res
        
        regular = helper(nums1, nums2)
        swapped = helper(nums1[:-1] + [nums2[-1]], nums2[:-1] + [nums1[-1]]) + 1

        return min(regular, swapped) if regular != float('inf') and swapped != float('inf') else -1
        
def main():
    sol = Solution()
    print(sol.minOperations(nums1 = [1,2,7], nums2 = [4,5,3]))
    print(sol.minOperations(nums1 = [2,3,4,5,9], nums2 = [8,8,4,4,4]))
    print(sol.minOperations(nums1 = [1,5,4], nums2 = [2,5,3]))

if __name__ == '__main__':
    main()