class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        prev_player_alice = False

        while x >= 1 and y >= 4:
            prev_player_alice = not prev_player_alice
            x -= 1
            y -= 4
        
        return "Alice" if prev_player_alice else "Bob"
        
def main():
    sol = Solution()
    print(sol.winningPlayer(x = 2, y = 7))
    print(sol.winningPlayer(x = 4, y = 11))

if __name__ == '__main__':
    main()