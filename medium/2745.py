class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return min(x + y + z, x + x + 1 + z, y + y + 1 + z) * 2
            
def main():
    sol = Solution()
    print(sol.longestString(x = 2, y = 5, z = 1))
    print(sol.longestString(x = 3, y = 2, z = 2))

if __name__ == '__main__':
    main()