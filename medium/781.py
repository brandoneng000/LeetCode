from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = {}
        res = 0

        for r in answers:
            if r == 0:
                res += 1
            elif rabbits.get(r, 0) == 0:
                res += r + 1
                rabbits[r] = r
            elif rabbits.get(r, 0) != 0:
                rabbits[r] -= 1
                
        return res

def main():
    sol = Solution()
    print(sol.numRabbits([1,1,2]))
    print(sol.numRabbits([10,10,10]))

if __name__ == '__main__':
    main()