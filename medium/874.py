from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        d = 0
        pos = [0, 0]
        blocks = set()
        for x, y in obstacles:
            blocks.add((x, y))
        
        for c in commands:
            if c == -1:
                d = (d + 1) % len(direction)
            elif c == -2:
                d = (d - 1) % len(direction)
            else:
                for _ in range(c):
                    if (pos[0] + direction[d][0], pos[1] + direction[d][1]) not in blocks:
                        pos[0] += direction[d][0]
                        pos[1] += direction[d][1]
                    else:
                        break
                res = max(res, (pos[0] * pos[0] + pos[1] * pos[1]))
        
        return res



def main():
    sol = Solution()
    print(sol.robotSim(commands = [4,-1,3], obstacles = []))
    print(sol.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
    print(sol.robotSim(commands = [6,-1,-1,6], obstacles = []))

if __name__ == '__main__':
    main()