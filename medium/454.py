from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1 = {}
        res = 0
        for i in nums1:
            for j in nums2:
                temp = -(i + j)
                sum1[temp] = sum1.get(temp, 0) + 1
        
        for i in nums3:
            for j in nums4:
                res += sum1.get(i + j, 0)
        return res

        
        # res = 0
        # for i in nums1:
        #     for j in nums2:
        #         for k in nums3:
        #             for l in nums4:
        #                 if i + j + k + l == 0:
        #                     res += 1
        
        # return res
    
def main():
    sol = Solution()
    print(sol.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
    print(sol.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))

if __name__ == '__main__':
    main()