from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        trip = [g - c for g, c in zip(gas, cost)]
        total_surplus, surplus = 0, 0
        start = 0

        for i in range(len(trip)):
            total_surplus += trip[i]
            surplus += trip[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
                    
        return -1 if (total_surplus < 0) else start

            

def main():
    sol = Solution()
    print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(sol.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))

if __name__ == '__main__':
    main()