from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memory = {}
        
        # def climb_floor(cost: List[int], floor: int) -> int:
        #     if floor < 0:
        #         return 0
            
        #     if floor == 0 or floor == 1:
        #         return cost[floor]
        #     if floor in memory:
        #         return memory[floor]
            
        #     memory[floor] = cost[floor] + min(climb_floor(cost, floor - 1), climb_floor(cost, floor - 2))
        #     return memory[floor]
            
        # return min(climb_floor(cost, len(cost) - 1), climb_floor(cost, len(cost) - 2))
        memory = {}
        for index in range(len(cost)):
            if index < 2:
                memory[index] = cost[index]
            else:
                memory[index] = cost[index] + min(memory[index - 1], memory[index - 2])
        
        return min(memory[len(cost) - 1], memory[len(cost) - 2])


def main():
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

if __name__ == '__main__':
    main()