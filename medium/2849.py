class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False

        dist = max(abs(sx - fx), abs(sy - fy))
        return dist <= t
        
def main():
    sol = Solution()
    print(sol.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6))
    print(sol.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3))

if __name__ == '__main__':
    main()