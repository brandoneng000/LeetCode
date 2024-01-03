from typing import List
from heapq import heappush, heappop

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 1000000007
        buy_backlog = []
        sell_backlog = []

        for p, a, order in orders:
            if order:
                while buy_backlog and -buy_backlog[0][0] >= p and a > 0:
                    b, amount = heappop(buy_backlog)
                    
                    if a > amount:
                        a -= amount
                    elif a < amount:
                        heappush(buy_backlog, [b, amount - a])
                        a = 0
                    else:
                        a = 0

                if a == 0:
                    continue

                heappush(sell_backlog, [p, a])
            else:
                while sell_backlog and sell_backlog[0][0] <= p and a > 0:
                    s, amount = heappop(sell_backlog)
                    
                    if a > amount:
                        a -= amount
                    elif a < amount:
                        heappush(sell_backlog, [s, amount - a])
                        a = 0
                    else:
                        a = 0
                
                if a == 0:
                    continue

                heappush(buy_backlog, [-p, a])
            
        return (sum(b[1] for b in buy_backlog) + sum(s[1] for s in sell_backlog)) % mod

        
def main():
    sol = Solution()
    print(sol.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))
    print(sol.getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))

if __name__ == '__main__':
    main()