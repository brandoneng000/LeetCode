from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dpA = [0] * n
        dpB = [0] * n
        
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        for i in range(1, n):
            dpA[i] = max(energyDrinkA[i] + dpA[i - 1], dpB[i- 1])
            dpB[i] = max(energyDrinkB[i] + dpB[i - 1], dpA[i - 1])
        
        return max(dpA[n - 1], dpB[n - 1])


        
def main():
    sol = Solution()
    print(sol.maxEnergyBoost(energyDrinkA = [5,5,6,3,4,3,3,4], energyDrinkB = [5,3,3,4,4,6,6,3]))
    print(sol.maxEnergyBoost(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]))
    print(sol.maxEnergyBoost(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]))

if __name__ == '__main__':
    main()