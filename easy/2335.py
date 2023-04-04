from typing import List
import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [-val for val in amount if val != 0]
        heapq.heapify(amount)
        res = 0
        while len(amount) > 1:
            cup_first = heapq.heappop(amount)
            cup_second = heapq.heappop(amount)
            cup_first += 1
            cup_second += 1
            res += 1
            if cup_first != 0:
                heapq.heappush(amount, cup_first)
            if cup_second != 0:
                heapq.heappush(amount, cup_second)
        
        if amount:
            return res + -amount[0]
        
        return res
        

def main():
    sol = Solution()
    print(sol.fillCups([1,4,2]))
    print(sol.fillCups([5,4,4]))
    print(sol.fillCups([5,0,0]))

if __name__ == '__main__':
    main()