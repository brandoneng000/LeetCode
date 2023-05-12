from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        index1, index2 = 0, 0

        while index1 < len(nums1) or index2 < len(nums2):
            if index1 == len(nums1):
                res.extend(nums2[index2:])
                index2 = len(nums2)
            elif index2 == len(nums2):
                res.extend(nums1[index1:])
                index1 = len(nums1)
            else:
                if nums1[index1][0] == nums2[index2][0]:
                    res.append([nums1[index1][0], nums1[index1][1] + nums2[index2][1]])
                    index1 += 1
                    index2 += 1
                elif nums1[index1][0] < nums2[index2][0]:
                    res.append(nums1[index1])
                    index1 += 1
                else:
                    res.append(nums2[index2])
                    index2 += 1

        return res
                    
        # nums = {}

        # for index, val in nums1:
        #     nums[index] = val
        
        # for index, val in nums2:
        #     nums[index] = nums.get(index, 0) + val
        
        # return sorted(list(nums.items()))


def main():
    sol = Solution()
    print(sol.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))
    print(sol.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))

if __name__ == '__main__':
    main()