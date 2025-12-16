from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        def dfs(u: int):
            cost = present[u]
            d_cost = present[u] // 2

            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            sub_profit0 = [0] * (budget + 1)
            sub_profit1 = [0] * (budget + 1)
            u_size = cost

            for v in graph[u]:
                child_dp0, child_dp1, vSize = dfs(v)
                u_size += vSize

                for i in range(budget, -1, -1):
                    for sub in range(min(vSize, i) + 1):
                        if i - sub >= 0:
                            sub_profit0[i] = max(sub_profit0[i], sub_profit0[i - sub] + child_dp0[sub])
                            sub_profit1[i] = max(sub_profit1[i], sub_profit1[i - sub] + child_dp1[sub])
            
            for i in range(budget + 1):
                dp0[i] = sub_profit0[i]
                dp1[i] = sub_profit0[i]

                if i >= d_cost:
                    dp1[i] = max(sub_profit0[i], sub_profit1[i - d_cost] + future[u] - d_cost)
                
                if i >= cost:
                    dp0[i] = max(sub_profit0[i], sub_profit1[i - cost] + future[u] - cost)
            
            return dp0, dp1, u_size

        graph = [[] for _ in range(n)]

        for a, b in hierarchy:
            graph[a - 1].append(b - 1)
        
        return dfs(0)[0][budget]


def main():
    sol = Solution()
    print(sol.maxProfit(n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3))
    print(sol.maxProfit(n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4))
    print(sol.maxProfit(n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10))

if __name__ == '__main__':
    main()