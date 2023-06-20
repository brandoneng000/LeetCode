from typing import List
import bisect

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)

        advantage = { n:[] for n in nums2 }
        remain = []
        res = []

        j = 0
        for n1 in sorted1:
            if n1 > sorted2[j]:
                advantage[sorted2[j]].append(n1)
                j += 1
            else:
                remain.append(n1)
        
        for n in nums2:
            if advantage[n]:
                res.append(advantage[n].pop())
            else:
                res.append(remain.pop())
        
        return res

    # def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     nums1.sort()
    #     res = [None] * len(nums1)

    #     for i, n in enumerate(nums2):
    #         index = bisect.bisect(nums1, n)
    #         if index < len(nums1):
    #             res[i] = nums1.pop(index)
        
    #     for i in range(len(res)):
    #         if res[i] is None:
    #             res[i] = nums1.pop()

    #     return res

        


def main():
    sol = Solution()
    print(sol.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))
    print(sol.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))

if __name__ == '__main__':
    main()