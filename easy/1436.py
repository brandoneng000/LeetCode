from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes = {}

        for path in paths:
            routes[path[0]] = path[1]

        dest = paths[0][0]
        while(dest in routes):
            dest = routes[dest]

        return dest
        
def main():
    sol = Solution()
    print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

if __name__ == '__main__':
    main()