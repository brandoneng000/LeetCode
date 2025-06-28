from typing import List
import heapq
import collections

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted([[num, i] for i, num in enumerate(nums)], reverse=True)[:k]
        sorted_nums.sort(key=lambda x: x[1])
        
        return [num for num, i in sorted_nums]


    # def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    #     return [num for num, i in sorted(sorted([[num, i] for i, num in enumerate(nums)], reverse=True)[:k], key=lambda x: x[1])]

    # def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    #     copy = nums.copy()
    #     size = len(copy)
    #     heapq.heapify(nums)
        
    #     while size > k:
    #         temp = heapq.heappop(nums)
    #         copy.remove(temp)
    #         size -= 1

    #     return copy

    # def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    #     heap = nums.copy()
    #     heapq.heapify(heap)
    #     largest = heapq.nlargest(k, heap)
    #     largest = collections.Counter(largest)
    #     result = []

    #     for num in nums:
    #         if num in largest and largest[num] > 0:
    #             result.append(num)
    #             largest[num] -= 1

    #     return result


def main():
    sol = Solution()
    print(sol.maxSubsequence(nums = [2,1,3,3], k = 2))
    print(sol.maxSubsequence(nums = [-1,-2,3,4], k = 3))
    print(sol.maxSubsequence(nums = [3,4,3,3], k = 2))

if __name__ == '__main__':
    main()