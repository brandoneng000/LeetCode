from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            part_a = (left + right) // 2
            part_b = (m + n + 1) // 2 - part_a

            max_left_a = -float('inf') if part_a == 0 else nums1[part_a - 1]
            min_right_a = float('inf') if part_a == m else nums1[part_a]
            max_left_b = -float('inf') if part_b == 0 else nums2[part_b - 1]
            min_right_b = float('inf') if part_b == n else nums2[part_b]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 0:
                    return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2
                else:
                    return max(max_left_a, max_left_b)
            elif max_left_a > min_right_b:
                right = part_a - 1
            else:
                left = part_a + 1
            

    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     if (len(nums1) + len(nums2)) % 2:
    #         return sorted(nums1 + nums2)[(len(nums1) + len(nums2)) // 2]
    #     else:
    #         return sum(sorted(nums1 + nums2)[(len(nums1) + len(nums2)) // 2 - 1: (len(nums1) + len(nums2)) // 2 + 1]) / 2
        
def main():
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
    print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
    print(sol.findMedianSortedArrays(nums1 = [1,2,3,4,5,6,7], nums2 = [3,4,6,7,8,89,94]))

if __name__ == '__main__':
    main()