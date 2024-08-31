from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        score1 = score2 = 0
        multi1 = multi2 = 0

        for p1, p2 in zip(player1, player2):
            score1 += p1 if multi1 <= 0 else 2 * p1
            score2 += p2 if multi2 <= 0 else 2 * p2

            multi1 -= 1
            multi2 -= 1

            if p1 == 10:
                multi1 = 2
            if p2 == 10:
                multi2 = 2
                

        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        
        return 0

        
def main():
    sol = Solution()
    print(sol.isWinner(player1 = [5,10,3,2], player2 = [6,5,7,3]))
    print(sol.isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2]))
    print(sol.isWinner(player1 = [2,3], player2 = [4,1]))
    print(sol.isWinner(player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]))

if __name__ == '__main__':
    main()