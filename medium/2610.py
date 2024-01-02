from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = [[] for i in range(max(count.values()))]

        for n in count:
            for i in range(count[n]):
                res[i].append(n)
        
        return res
        
def main():
    sol = Solution()
    print(sol.findMatrix([1,3,4,1,2,3,1]))
    print(sol.findMatrix([1,2,3,4]))

if __name__ == '__main__':
    main()