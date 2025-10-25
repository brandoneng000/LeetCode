from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def compare_nums(x: str, y: str):
            diff = 0

            for i, j in zip(x, y):
                diff += i != j
            
            return diff <= 2

        numbers = defaultdict(list)
        digits = len(str(max(nums)))
        res = 0

        for num in nums:
            num = f"{num:0{digits}}"
            digits_sorted = ''.join(sorted(num))
            numbers[digits_sorted].append(num)

        for num in numbers:
            n = len(numbers[num])

            for i in range(n):
                for j in range(i + 1, n):
                    res += compare_nums(numbers[num][i], numbers[num][j])
        
        return res

        
def main():
    sol = Solution()
    print(sol.countPairs([3,12,30,17,21]))
    print(sol.countPairs([1,1,1,1,1]))
    print(sol.countPairs([123,231]))

if __name__ == '__main__':
    main()