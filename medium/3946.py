from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = min(price for _, price in items)

        for factor, price in items:
            cnt = sum(
                1 for other_factor, _ in items if other_factor % factor == 0
            )

            for j in range(budget, price - 1, -1):
                if f[j - price] + cnt > f[j]:
                    f[j] = f[j - price] + cnt

        return max(f[j] + (budget - j) // mn for j in range(budget + 1))

def main():
    sol = Solution()
    print(sol.maximumSaleItems(items = [[6,2],[2,6],[3,4]], budget = 9))
    print(sol.maximumSaleItems(items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8))

if __name__ == '__main__':
    main()