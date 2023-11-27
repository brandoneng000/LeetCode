from typing import List
from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 1000000007
        count = Counter()
        res = 0

        for food in deliciousness:
            for i in range(22):
                res += count[2 ** i - food]
            count[food] += 1
            
        return res % mod

        
def main():
    sol = Solution()
    print(sol.countPairs([1,3,5,7,9]))
    print(sol.countPairs([1,1,1,3,3,3,7]))

if __name__ == '__main__':
    main()