class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        route = [pos]

        for dir in path:
            if dir == 'N':
                pos = (pos[0], pos[1] + 1)
            elif dir == 'S':
                pos = (pos[0], pos[1] - 1)
            elif dir == 'E':
                pos = (pos[0] + 1, pos[1])
            else:
                pos = (pos[0] - 1, pos[1])
            
            if pos in route:
                return True
            else:
                route.append(pos)
        
        return False


def main():
    sol = Solution()
    print(sol.isPathCrossing("NES"))
    print(sol.isPathCrossing("NESWW"))

if __name__ == '__main__':
    main()