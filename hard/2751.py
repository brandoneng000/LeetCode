from typing import List
from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        line = sorted([p, r, h, d] for r, [p, h, d] in enumerate(zip(positions, healths, directions), 1))
        stack = deque()
        res = {}

        for p, r, h, d in line:
            if not stack:
                stack.append([p, r, h, d])
            else:
                if stack[-1][3] == d:
                    stack.append([p, r, h, d])
                else:
                    while stack and h:
                        if stack[-1][2] > h:
                            stack[-1][2] -= 1
                            h = 0
                        elif stack[-1][2] < h:
                            stack.pop()
                            h -= 1
                        else:
                            stack.pop()
                            h = 0
                    if h:
                        stack.append([p, r, h, d])
            
            while stack and stack[0][3] == 'L':
                res[stack[0][1]] = stack[0][2]
                stack.popleft()
            
        for p, r, h, d in stack:
            res[r] = h

        return [res[r] for r in sorted(res)]
        
def main():
    sol = Solution()
    print(sol.survivedRobotsHealths(positions = [1, 40], healths = [10,11], directions = "RL"))
    print(sol.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))
    print(sol.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))
    print(sol.survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"))

if __name__ == '__main__':
    main()