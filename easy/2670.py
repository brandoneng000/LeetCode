from typing import List
from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix_count = Counter(nums)
        prefix_count = Counter()
        res = []

        for num in nums:
            suffix_count[num] -= 1
            
            if suffix_count[num] == 0:
                del suffix_count[num]
            
            prefix_count[num] += 1
            res.append(len(prefix_count) - len(suffix_count))
        
        return res
        
def main():
    sol = Solution()
    print(sol.distinctDifferenceArray([1,2,3,4,5]))
    print(sol.distinctDifferenceArray([3,2,3,4,2]))

if __name__ == '__main__':
    main()