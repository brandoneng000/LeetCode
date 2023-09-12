class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = 0 if x1 <= xCenter <= x2 else min(abs(x1 - xCenter), abs(x2 - xCenter))
        y = 0 if y1 <= yCenter <= y2 else min(abs(y1 - yCenter), abs(y2 - yCenter))
        
        return x * x + y * y <= radius * radius

        

def main():
    sol = Solution()
    print(sol.checkOverlap(radius = 5, xCenter = 8, yCenter = 8, x1 = 9, y1 = 5, x2 = 12, y2 = 8))
    print(sol.checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
    print(sol.checkOverlap(radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
    print(sol.checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))

if __name__ == '__main__':
    main()