from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []
    #     num_set = set()
    #     short = nums1 if len(nums1) <= len(nums2) else nums2
    #     long = nums1 if len(nums1) > len(nums2) else nums2

    #     for num in short:
    #         num_set.add(num)

    #     for num in num_set:
    #         if num in long:
    #             res.append(num)
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))
    print(sol.intersection([4,9,5], [9,4,9,8,4]))

if __name__ == '__main__':
    main()