from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        i = j = 0
        res = []

        while i < n:
            if nums[i] == key:
                while j < n and j < i + k + 1:
                    res.append(j)
                    j += 1
            
            while i - j >= k:
                j += 1
            
            i += 1
        
        return res


    # def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
    #     res = set()

    #     for index, val in enumerate(nums):
    #         if key == val:
    #             for i in range(max(index - k, 0), min(len(nums), index + k + 1)):
    #                 res.add(i)
        
    #     return sorted(list(res))


def main():
    sol = Solution()
    print(sol.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
    print(sol.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))

if __name__ == '__main__':
    main()