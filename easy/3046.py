from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num in count:
            if count[num] > 2:
                return False

        return True
        
def main():
    sol = Solution()
    print(sol.isPossibleToSplit([1,1,2,2,3,4]))
    print(sol.isPossibleToSplit([1,1,1,1]))

if __name__ == '__main__':
    main()