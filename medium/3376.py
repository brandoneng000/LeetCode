from typing import List
from itertools import permutations

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        INF = 10 ** 33
        res = INF

        for perm in permutations(strength):
            t = 0
            x = 1

            for str in perm:
                t += (str + x - 1) // x
                x += k

            res = min(res, t)
        
        return res

def main():
    sol = Solution()
    print(sol.findMinimumTime(strength = [3,4,1], k = 1))
    print(sol.findMinimumTime(strength = [2,5,4], k = 2))

if __name__ == '__main__':
    main()