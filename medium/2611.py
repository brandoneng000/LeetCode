from typing import List
from heapq import heappush, heappop

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        heap = []
        eaten = set()
        res = 0

        for i in range(n):
            heappush(heap, (reward2[i] - reward1[i], i))

        while k:
            diff, index = heappop(heap)
            res += reward1[index]
            eaten.add(index)
            k -= 1
        
        return res + sum([reward2[i] for i in range(n) if i not in eaten])
        
def main():
    sol = Solution()
    print(sol.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))
    print(sol.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2))

if __name__ == '__main__':
    main()