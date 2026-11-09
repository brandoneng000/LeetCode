from typing import List
from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        res = [0] * k
        busy = []
        free = list(range(k))

        for i in range(n):
            time = arrival[i]
            duration = load[i]

            while busy and busy[0][0] <= time:
                heappush(free, i + (heappop(busy)[1] - i) % k)

            if free:
                x = heappop(free) % k
                heappush(busy, (time + duration, x))
                res[x] += 1

        most_req = max(res)
        return [i for i in range(k) if res[i] == most_req]



def main():
    sol = Solution()
    print(sol.busiestServers(k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] ))
    print(sol.busiestServers(k = 3, arrival = [1,2,3,4], load = [1,2,1,2]))
    print(sol.busiestServers(k = 3, arrival = [1,2,3], load = [10,12,11]))

if __name__ == '__main__':
    main()