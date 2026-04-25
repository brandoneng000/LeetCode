from typing import List
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def check(limit: int):
            perimeter = side * 4

            for start in arr:
                end = start + perimeter - limit
                cur = start

                for _ in range(k - 1):
                    index = bisect_left(arr, cur + limit)

                    if index == len(arr) or arr[index] > end:
                        cur = -1
                        break
                    
                    cur = arr[index]

                if cur >= 0:
                    return True
                
            return False

        arr = []
        res = 0

        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(side * 3 - y)
            else:
                arr.append(side * 4 - x)
            
        arr.sort()

        left, right = 1, side

        while left <= right:
            middle = (left + right) // 2

            if check(middle):
                left = middle + 1
                res = middle
            else:
                right = middle - 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxDistance(side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4))
    print(sol.maxDistance(side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4))
    print(sol.maxDistance(side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5))

if __name__ == '__main__':
    main()