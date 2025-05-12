# import collections
from typing import List
from collections import Counter


class Solution:
    # def findEvenNumbers(self, digits: List[int]) -> List[int]:
    #     n = len(digits)
    #     res = set()

    #     for i in range(n):
    #         for j in range(n):
    #             for k in range(n):
    #                 if i == j or j == k or i == k:
    #                     continue

    #                 num = digits[i] * 100 + digits[j] * 10 + digits[k]

    #                 if num >= 100 and num % 2 == 0:
    #                     res.add(num)
        
    #     return sorted(res)

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def digit_counter(num: int) -> Counter:
            count = Counter()

            for digit in str(num):
                count[int(digit)] += 1
            
            return count
        
        res = []
        digits_count = Counter(digits)

        for num in range(100, 1000, 2):
            if not digit_counter(num) - digits_count:
                res.append(num)
        
        return res

    # def findEvenNumbers(self, digits: List[int]) -> List[int]:
    #     result = []

    #     digits_count = collections.Counter(digits)
    #     for num in range(100, 1000, 2):
    #         if not collections.Counter(int(d) for d in str(num)) - digits_count:
    #             result.append(num)
        
    #     return result


def main():
    sol = Solution()
    print(sol.findEvenNumbers([2,1,3,0]))
    print(sol.findEvenNumbers([2,2,8,8,2]))
    print(sol.findEvenNumbers([3,7,5]))

if __name__ == '__main__':
    main()