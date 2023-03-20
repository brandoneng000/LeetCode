from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result = 0
        cost.sort(reverse=True)

        for index in range(0, len(cost), 3):
            result += cost[index]
            result += cost[index + 1] if index + 1 < len(cost) else 0
        
        return result

def main():
    sol = Solution()
    print(sol.minimumCost([1,2,3]))
    print(sol.minimumCost([6,5,7,9,2,2]))
    print(sol.minimumCost([5,5]))

if __name__ == '__main__':
    main()