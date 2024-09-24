class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # check rook
        if a == e:
            if c == a and (b < d < f or f < d < b):
                pass
            else:
                return 1
        
        if b == f:
            if d == b and (a < c < e or e < c < a):
                pass
            else:
                return 1
        
        #check bishop
        for i in range(1, 9):
            if c + i == a and d + i == b:
                break
            elif c + i == e and d + i == f:
                return 1
        
        for i in range(-1, -9, -1):
            if c + i == a and d + i == b:
                break
            elif c + i == e and d + i == f:
                return 1
        
        for i in range(1, 9):
            j = -i

            if c + i == a and d + j == b:
                break
            elif c + i == e and d + j == f:
                return 1
        
        for i in range(1, 9):
            j = -i

            if c + j == a and d + i == b:
                break
            elif c + j == e and d + i == f:
                return 1

        return 2

def main():
    sol = Solution()
    print(sol.minMovesToCaptureTheQueen(a = 1, b = 1, c = 8, d = 8, e = 2, f = 3))
    print(sol.minMovesToCaptureTheQueen(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2))

if __name__ == '__main__':
    main()