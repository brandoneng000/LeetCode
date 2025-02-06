from typing import List
from heapq import heappush, heappop

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        res = 0
        marked_enemy = [False] * n
        min_heap = []
        max_heap = []

        for i in range(n):
            heappush(min_heap, (enemyEnergies[i], i))
            heappush(max_heap, (-enemyEnergies[i], i))
        
        while (min_heap and currentEnergy >= min_heap[0][0]) or (max_heap and res):
            while currentEnergy < min_heap[0][0] and max_heap and res:
                energy, index = heappop(max_heap)

                if marked_enemy[index]:
                    continue

                marked_enemy[index] = True
                currentEnergy += -energy
            
            if marked_enemy[min_heap[0][1]]:
                heappop(min_heap)
                continue
            else:
                quotient, remainder = divmod(currentEnergy, min_heap[0][0])
                res += quotient
                currentEnergy = remainder
                

        return res


        
def main():
    sol = Solution()
    print(sol.maximumPoints(enemyEnergies = [3,2,2], currentEnergy = 2))
    print(sol.maximumPoints(enemyEnergies = [2], currentEnergy = 10))

if __name__ == '__main__':
    main()