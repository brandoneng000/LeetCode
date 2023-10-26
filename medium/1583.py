from typing import List
import bisect

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n == 2:
            return 0
        
        pref = {}

        for x, y in pairs:
            pref[x] = preferences[x][:preferences[x].index(y)]
            pref[y] = preferences[y][:preferences[y].index(x)]
        
        res = 0
        for person, friends in pref.items():
            for friend in friends:
                if person in pref[friend]:
                    res += 1
                    break
        
        return res
        

        
def main():
    sol = Solution()
    print(sol.unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]))
    print(sol.unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]]))
    print(sol.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))

if __name__ == '__main__':
    main()