from typing import List
from math import ceil

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        steps = [ceil(d / s) for d, s in zip(dist, speed)]
        steps.sort()

        for i in range(n):
            if i >= steps[i]:
                return i
        
        return n
        
def main():
    sol = Solution()
    print(sol.eliminateMaximum(dist = [1,3,4], speed = [1,1,1]))
    print(sol.eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1]))
    print(sol.eliminateMaximum(dist = [3,2,4], speed = [5,3,2]))

if __name__ == '__main__':
    main()