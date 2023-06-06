from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist_player = abs(target[0]) + abs(target[1]) 

        for ghost in ghosts:
            dist_ghost = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if dist_player >= dist_ghost:
                return False
            
        return True


def main():
    sol = Solution()
    print(sol.escapeGhosts(ghosts = [[1,8],[-9,0],[-7,-6],[4,3],[1,3]], target = [6,-9]))
    print(sol.escapeGhosts(ghosts = [[1,0],[0,3]], target = [0,1]))
    print(sol.escapeGhosts(ghosts = [[1,0]], target = [2,0]))
    print(sol.escapeGhosts(ghosts = [[2,0]], target = [1,0]))

if __name__ == '__main__':
    main()