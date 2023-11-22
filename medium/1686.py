from typing import List
from heapq import heappush, heappop

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        alice_turn = True
        alice = 0
        bob = 0
        heap = []

        for i in range(n):
            heappush(heap, (-(aliceValues[i] + bobValues[i]), aliceValues[i], bobValues[i]))
        
        while heap:
            points, a, b = heappop(heap)

            if alice_turn:
                alice += a
            else:
                bob += b
            
            alice_turn = not alice_turn
            
        if alice == bob:
            return 0
        
        return 1 if alice > bob else -1

        
def main():
    sol = Solution()
    print(sol.stoneGameVI(aliceValues = [1,3], bobValues = [2,1]))
    print(sol.stoneGameVI(aliceValues = [1,2], bobValues = [3,1]))
    print(sol.stoneGameVI(aliceValues = [2,4,3], bobValues = [1,6,7]))

if __name__ == '__main__':
    main()