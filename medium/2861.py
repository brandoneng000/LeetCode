from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0

        for i in range(k):
            left = 0
            right = 2 * 10 ** 9

            while left <= right:
                middle = (left + right) // 2
                price = 0

                for j in range(n):
                    req = composition[i][j] * middle
                    req -= stock[j]

                    if req >= 0:
                        price += req * cost[j]

                if price <= budget:
                    res = max(res, middle)
                    left = middle + 1
                else:
                    right = middle - 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]))
    print(sol.maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]))
    print(sol.maxNumberOfAlloys(n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]))

if __name__ == '__main__':
    main()