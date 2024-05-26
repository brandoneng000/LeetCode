from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        i = j = 0
        res = 0

        while i < len(players) and j < len(trainers):
            if players[i] > trainers[j]:
                j += 1
            else:
                res += 1
                i += 1
                j += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8]))
    print(sol.matchPlayersAndTrainers(players = [1,1,1], trainers = [10]))

if __name__ == '__main__':
    main()