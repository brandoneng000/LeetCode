from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        travel = [0] * 1001

        for c, p, d in trips:
            travel[p] += c
            travel[d] -= c
        
        for i in range(len(travel)):
            if capacity < 0:
                return False
            capacity -= travel[i]

        return True

    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #     travel = [0] * 1000
        
    #     pick_up = {}
    #     drop_off = {}

    #     for c, p, d in trips:
    #         pick_up[p] = pick_up.get(p, 0) + c
    #         drop_off[d] = drop_off.get(d, 0) - c
        
    #     for i in range(len(travel)):
    #         travel[i] = travel[i - 1] + pick_up.get(i, 0) + drop_off.get(i, 0)
    #         if travel[i] > capacity:
    #             return False
        
    #     return True


def main():
    sol = Solution()
    print(sol.carPooling(trips = [[9,0,1],[3,3,7]], capacity = 4))
    print(sol.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
    print(sol.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))

if __name__ == '__main__':
    main()