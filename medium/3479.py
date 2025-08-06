from typing import List
from math import isqrt

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = isqrt(n)
        section = (n + m - 1) // m
        res = 0
        max_val = [0] * section

        for i in range(n):
            max_val[i // m] = max(max_val[i // m], baskets[i])

        for fruit in fruits:
            unset = 1

            for sec in range(section):
                if max_val[sec] < fruit:
                    continue

                choose = 0
                max_val[sec] = 0

                for i in range(m):
                    pos = sec * m + i

                    if pos < n and baskets[pos] >= fruit and not choose:
                        baskets[pos] = 0
                        choose = 1
                    
                    if pos < n:
                        max_val[sec] = max(max_val[sec], baskets[pos])
                unset = 0
                break
            res += unset

        return res

        
def main():
    sol = Solution()
    print(sol.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
    print(sol.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))

if __name__ == '__main__':
    main()