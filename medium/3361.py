from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        def shift_dist_next(start: int, goal: int, cost: List[int]):
            res = 0
            index = start

            for i in range(1, 26):
                res += cost[index]
                index = (start + i) % 26

                if index == goal:
                    break
            
            return res
        
        def shift_dist_prev(start: int, goal: int, cost: List[int]):
            res = 0
            index = start

            for i in range(1, 26):
                res += cost[index]
                index = (start - i) % 26

                if index == goal:
                    break
            
            return res


        n = len(s)
        res = 0
        a = ord('a')

        for i in range(n):
            if s[i] == t[i]:
                continue
            
            nxt = shift_dist_next(ord(s[i]) - a, ord(t[i]) - a, nextCost)
            prv = shift_dist_prev(ord(s[i]) - a, ord(t[i]) - a, previousCost)
            res += min(nxt, prv)
        
        return res

        
def main():
    sol = Solution()
    print(sol.shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(sol.shiftDistance(s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

if __name__ == '__main__':
    main()