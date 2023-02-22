from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largest_square = 0
        square_count = 0

        for rect in rectangles:
            square = min(rect)
            if largest_square == square:
                square_count += 1
            elif square > largest_square:
                largest_square = square
                square_count = 1
        
        return square_count

def main():
    sol = Solution()
    print(sol.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))
    print(sol.countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]))

if __name__ == '__main__':
    main()