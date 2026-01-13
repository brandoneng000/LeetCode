from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(y0):
            area = 0

            for x, y, l in squares:
                if y < y0:
                    area += l * min(y0 - y, l)
            
            return area >= total_area / 2
        
        low = 0
        high = -float('inf')
        eps = 1e-5
        total_area = 0

        for x, y, l in squares:
            total_area += l * l
            high = max(high, y + l)
        
        while abs(high - low) > eps:
            middle = (low + high) / 2

            if check(middle):
                high = middle
            else:
                low = middle
        
        return high

        
def main():
    sol = Solution()
    print(sol.separateSquares([[0,0,1],[2,2,1]]))
    print(sol.separateSquares([[0,0,2],[1,1,1]]))

if __name__ == '__main__':
    main()