from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        res = n - 1
        stockPrices.sort()

        for i in range(1, n - 1):
            a, b, c = stockPrices[i - 1], stockPrices[i], stockPrices[i + 1]

            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        
        return res



def main():
    sol = Solution()
    print(sol.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
    print(sol.minimumLines([[3,4],[1,2],[7,8],[2,3]]))

if __name__ == '__main__':
    main()