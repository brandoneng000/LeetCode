from typing import List
from collections import Counter

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        smallest = min(count)
        
        for i in count:
            temp = i % smallest

            if temp not in count and temp < smallest and temp != 0:
                return 1
                
        return count[smallest] // 2 + count[smallest] % 2
        
def main():
    sol = Solution()
    print(sol.minimumArrayLength([1,4,3,1]))
    print(sol.minimumArrayLength([5,5,5,10,5]))
    print(sol.minimumArrayLength([2,3,4]))

if __name__ == '__main__':
    main()