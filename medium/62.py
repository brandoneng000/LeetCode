class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row

        return row[0]



def main():
    sol = Solution()
    print(sol.uniquePaths(3, 7))
    print(sol.uniquePaths(3, 2))

if __name__ == '__main__':
    main()