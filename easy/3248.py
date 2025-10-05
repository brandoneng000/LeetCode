from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0

        for c in commands:
            if c == "UP":
                res -= n
            elif c == "DOWN":
                res += n
            elif c == "RIGHT":
                res += 1
            elif c == "LEFT":
                res -= 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.finalPositionOfSnake(n = 2, commands = ["RIGHT","DOWN"]))
    print(sol.finalPositionOfSnake(n = 3, commands = ["DOWN","RIGHT","UP"]))

if __name__ == '__main__':
    main()