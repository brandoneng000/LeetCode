from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        vals = sorted([a, b, c])

        smallest = 2
        if vals[1] - vals[0] == 2 or vals[2] - vals[1] == 2 or vals[1] - vals[0] == 1 or vals[2] - vals[1] == 1:
            smallest = 1
            
        if vals[0] + 1 == vals[1] and vals[1] + 1 == vals[2]:
            smallest = 0
        

        return [smallest, (vals[1] - vals[0] - 1) + (vals[2] - vals[1] - 1)]

def main():
    sol = Solution()
    print(sol.numMovesStones(1, 2, 5))
    print(sol.numMovesStones(4, 3, 2))
    print(sol.numMovesStones(3, 5, 1))

if __name__ == '__main__':
    main()