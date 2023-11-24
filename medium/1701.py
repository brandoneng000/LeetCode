from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = cur = 0

        for arrive, time in customers:
            cur = max(cur, arrive) + time
            wait += cur - arrive

        return wait / len(customers)

    # def averageWaitingTime(self, customers: List[List[int]]) -> float:
    #     n = len(customers)
    #     res = [(0, 0)]

    #     for arrive, time in customers:
    #         if arrive >= res[-1][1]:
    #             res.append((arrive, arrive + time))
    #         else:
    #             res.append((arrive, res[-1][1] + time))
        
    #     return sum(finish - arrive for arrive, finish in res) / n


        
def main():
    sol = Solution()
    print(sol.averageWaitingTime([[1,2],[2,5],[4,3]]))
    print(sol.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))

if __name__ == '__main__':
    main()