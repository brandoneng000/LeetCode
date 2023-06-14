from typing import List
import collections

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        room_keys = { i: rooms[i] for i in range(len(rooms)) }
        visited = set()
        
        def helper(key: int):
            visited.add(key)
            for i in room_keys[key]:
                if i not in visited:
                    helper(i)
        
        helper(0)
        return len(visited) == n



def main():
    sol = Solution()
    print(sol.canVisitAllRooms([[1],[2],[3],[]]))
    print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

if __name__ == '__main__':
    main()