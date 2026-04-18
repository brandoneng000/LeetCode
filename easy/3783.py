class Solution:
    def mirrorDistance(self, n: int) -> int:
        def flip_num(num: int):
            return int(str(num)[::-1])
        
        return abs(n - flip_num(n))
        
def main():
    sol = Solution()
    print(sol.mirrorDistance(25))
    print(sol.mirrorDistance(10))
    print(sol.mirrorDistance(7))

if __name__ == '__main__':
    main()