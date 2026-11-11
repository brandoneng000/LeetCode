class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 < costBoth:
            costBoth = cost1 + cost2

        if cost1 > costBoth and cost2 > costBoth:
            return costBoth * max(need1, need2)
        if cost1 > costBoth:
            cost1 = costBoth
        if cost2 > costBoth:
            cost2 = costBoth

        both = min(need1, need2)

        return costBoth * both + cost1 * (need1 - both) + cost2 * (need2 - both)

def main():
    sol = Solution()
    print(sol.minimumCost(cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2))
    print(sol.minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3))
    print(sol.minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0))

if __name__ == '__main__':
    main()