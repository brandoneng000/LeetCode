class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0

        for i in range(total // cost1 + 1):
            cur = total - (i * cost1)
            res += cur // cost2 + 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.waysToBuyPensPencils(total = 20, cost1 = 10, cost2 = 5))
    print(sol.waysToBuyPensPencils(total = 5, cost1 = 10, cost2 = 10))

if __name__ == '__main__':
    main()