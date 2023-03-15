import collections
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []

        digits_count = collections.Counter(digits)
        for num in range(100, 1000, 2):
            if not collections.Counter(int(d) for d in str(num)) - digits_count:
                result.append(num)
        
        return result


def main():
    sol = Solution()
    print(sol.findEvenNumbers([2,1,3,0]))
    print(sol.findEvenNumbers([2,2,8,8,2]))
    print(sol.findEvenNumbers([3,7,5]))

if __name__ == '__main__':
    main()