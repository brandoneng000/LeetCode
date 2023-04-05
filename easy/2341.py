from typing import List
import collections

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_count = collections.Counter(nums)
        pairs = remainder = 0

        for num in nums_count:
            p, r = divmod(nums_count[num], 2)
            pairs += p
            remainder += r
        
        return [pairs, remainder]

def main():
    sol = Solution()
    print(sol.numberOfPairs([1,3,2,1,3,2,2]))
    print(sol.numberOfPairs([1,1]))
    print(sol.numberOfPairs([0]))

if __name__ == '__main__':
    main()