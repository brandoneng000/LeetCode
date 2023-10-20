from typing import List
import bisect

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(middle: int):
            res = 1
            cur = position[0]

            for i in range(1, n):
                if position[i] - cur >= middle:
                    res += 1
                    cur = position[i]
            return res
        
        left, right = 0, position[-1] - position[0]

        while left < right:
            middle = right - (right - left) // 2
            
            if count(middle) >= m:
                left = middle
            else:
                right = middle - 1
        
        return left


def main():
    sol = Solution()
    print(sol.maxDistance(position = [1,2,3,4,7], m = 3))
    print(sol.maxDistance(position = [5,4,3,2,1,1000000000], m = 2))

if __name__ == '__main__':
    main()