from typing import List, Counter
import collections

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_factors(squares: List[int], nums: List[int]) -> int:
            res = 0

            for sq in squares:
                count = collections.Counter()

                for n in nums:
                    if sq % n == 0:
                        res += count[sq // n]
                    count[n] += 1
            
            return res
        
        squares1 = [num * num for num in nums1]
        squares2 = [num * num for num in nums2]

        return count_factors(squares1, nums2) + count_factors(squares2, nums1)

    # def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    #     def count_factors(squares: Counter, nums: List[int]) -> int:
    #         res = 0

    #         for sq in squares:
    #             for i in range(len(nums)):
    #                 for j in range(i + 1, len(nums)):
    #                     if sq == nums[i] * nums[j]:
    #                         res += squares[sq]
            
    #         return res

    #     squares1 = collections.Counter([num * num for num in nums1])
    #     squares2 = collections.Counter([num * num for num in nums2])
        
    #     return count_factors(squares1, nums2) + count_factors(squares2, nums1)

        

        
def main():
    sol = Solution()
    print(sol.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]))
    print(sol.numTriplets(nums1 = [1,1], nums2 = [1,1,1]))
    print(sol.numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]))

if __name__ == '__main__':
    main()