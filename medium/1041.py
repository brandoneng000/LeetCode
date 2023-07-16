import collections

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        facing = 0

        for i in instructions:
            if i == 'G':
                x, y = x + directions[facing][0], y + directions[facing][1]
            elif i == 'R':
                facing = (facing + 1) % 4
            elif i == 'L':
                facing = (facing - 1) % 4

        return (x, y) == (0, 0) or facing != 0


def main():
    sol = Solution()
    print(sol.isRobotBounded("GGLLGG"))
    print(sol.isRobotBounded("GG"))
    print(sol.isRobotBounded("GL"))

if __name__ == '__main__':
    main()