from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        province = 0

        def dfs(city: int):
            visited.add(city)
            for j in range(len(isConnected[city])):
                if j not in visited and isConnected[city][j] == 1:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                province += 1
                dfs(i)

        return province


def main():
    sol = Solution()
    print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))

if __name__ == '__main__':
    main()