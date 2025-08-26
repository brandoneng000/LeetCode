class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def solve(red: int, blue: int):
            res = 0

            for i in range(1, 100):
                if i % 2 == 1 and red >= i:
                    red -= i
                elif i % 2 == 0 and blue >= i:
                    blue -= i
                else:
                    break
                res += 1
            
            return res
        
        return max(solve(red, blue), solve(blue, red))
        
def main():
    sol = Solution()
    print(sol.maxHeightOfTriangle(red = 2, blue = 4))
    print(sol.maxHeightOfTriangle(red = 2, blue = 1))
    print(sol.maxHeightOfTriangle(red = 1, blue = 1))
    print(sol.maxHeightOfTriangle(red = 10, blue = 1))

if __name__ == '__main__':
    main()