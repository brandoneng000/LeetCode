class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone_remove = 10
        alice_turn = True

        while n - stone_remove >= 0:
            if alice_turn:
                n -= stone_remove
            else:
                n -= stone_remove
            
            stone_remove -= 1
            alice_turn = not alice_turn
        
        return not alice_turn
        

def main():
    sol = Solution()
    print(sol.canAliceWin(27))
    print(sol.canAliceWin(10))
    print(sol.canAliceWin(12))
    print(sol.canAliceWin(1))

if __name__ == '__main__':
    main()