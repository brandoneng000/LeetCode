from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = [False] * n
        turn = 1
        index = 0

        while True:
            if not players[index]:
                players[index] = True
            else:
                break

            index = (index + turn * k) % n
            turn += 1
        
        return [i + 1 for i in range(n) if not players[i]]

        
def main():
    sol = Solution()
    print(sol.circularGameLosers(n = 5, k = 2))
    print(sol.circularGameLosers(n = 4, k = 4))

if __name__ == '__main__':
    main()