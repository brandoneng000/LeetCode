from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        instruction = len(s)
        directions = { 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0) }
        res = []

        for i in range(instruction):
            row, col = startPos
            for j in range(i, instruction):
                dr, dc = directions[s[j]]
                if 0 <= row + dr < n and 0 <= col + dc < n:
                    row += dr
                    col += dc
                else:
                    break
            else:
                j += 1
            res.append(j - i)
        
        return res

        
def main():
    sol = Solution()
    print(sol.executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU"))
    print(sol.executeInstructions(n = 2, startPos = [1,1], s = "LURD"))
    print(sol.executeInstructions(n = 1, startPos = [0,0], s = "LRUD"))

if __name__ == '__main__':
    main()