from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        occ = {}
        first_app = {}
        degree = 0
        min_length = 50000

        for index, val in enumerate(nums):
            if val not in first_app:
                first_app[val] = index
            occ[val] = occ.get(val, 0) + 1

            if occ[val] > degree:
                degree = occ[val]
                min_length = index - first_app[val] + 1
            elif degree == occ[val]:
                min_length = min(min_length, index - first_app[val] + 1)

        return min_length
            

            

def main():
    sol = Solution()
    print(sol.findShortestSubArray(nums = [1,2,2,3,1]))
    print(sol.findShortestSubArray([1,2,2,3,1,4,2]))
    print(sol.findShortestSubArray(nums = [1,2,2,3,1,4,4,4,4,4]))

if __name__ == '__main__':
    main()