from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        evens = Counter()
        odds = Counter()
        total = 0
        res = n

        for i in range(0, n, 2):
            evens[nums[i]] += 1
            total += 1

        evens[0] = 0
        
        for i in range(1, n, 2):
            odds[nums[i]] += 1
            total += 1
        
        odds[0] = 0

        c1 = evens.most_common(2)
        c2 = odds.most_common(2)

        for num1, freq1 in c1:
            for num2, freq2 in c2:
                if num1 != num2:
                    res = min(res, n - (freq1 + freq2))
        
        return res


        
def main():
    sol = Solution()
    print(sol.minimumOperations([3,1,3,2,4,3]))
    print(sol.minimumOperations([1,2,2,2,2]))

if __name__ == '__main__':
    main()