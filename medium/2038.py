class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = bob = 0
        cur = ''
        count = 0

        for c in colors:
            if cur != c:
                if cur == 'A':
                    alice += max(0, count - 2)
                elif cur == 'B':
                    bob += max(0, count - 2)
                cur = c
                count = 1
            else:
                count += 1

        if cur == 'A':
            alice += max(0, count - 2)
        elif cur == 'B':
            bob += max(0, count - 2)
            
        return alice > bob

def main():
    sol = Solution()
    print(sol.winnerOfGame("AAAABBBB"))
    print(sol.winnerOfGame("AAABABB"))
    print(sol.winnerOfGame("AA"))
    print(sol.winnerOfGame("ABBBBBBBAAA"))

if __name__ == '__main__':
    main()