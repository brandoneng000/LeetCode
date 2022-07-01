from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = [float("inf")] * (amount + 1)
        total[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    total[a] = min(total[a], 1 + total[a -c])

        return total[amount] if total[amount] != float("inf") else -1


def main():
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))
    print(sol.coinChange([2], 3))
    print(sol.coinChange([1], 0))
    print(sol.coinChange([2,5,10,1], 27))
    print(sol.coinChange([186,419,83,408], 6249))

if __name__ == '__main__':
    main()