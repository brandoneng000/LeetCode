class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0

        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n :
                        res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.distributeCandies(n = 5, limit = 2))
    print(sol.distributeCandies(n = 3, limit = 3))

if __name__ == '__main__':
    main()