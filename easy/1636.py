from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        return sorted(nums, key=lambda x: (count[x], -x))


    # def frequencySort(self, nums: List[int]) -> List[int]:
    #     nums_count = collections.Counter(nums)
    #     occurences = collections.defaultdict(list)
    #     result = []

    #     for num in nums_count:
    #         occurences[nums_count[num]].append(num)
        
    #     for occ in sorted(occurences):
    #         occurences[occ].sort(reverse=True)
    #         for num in occurences[occ]:
    #             result += [num] * occ
        
    #     return result
        

def main():
    sol = Solution()
    print(sol.frequencySort([1,1,2,2,2,3]))
    print(sol.frequencySort([2,3,1,3,2]))
    print(sol.frequencySort([-1,1,-6,4,5,-6,1,4,1]))
    print(sol.frequencySort([1,5,0,5]))

if __name__ == '__main__':
    main()