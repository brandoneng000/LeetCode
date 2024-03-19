class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def check(s: str, locked: str, op: str):
            free = 0
            balance = 0

            for i in range(len(s)):
                if locked[i] == '0':
                    free += 1
                else:
                    balance += 1 if s[i] == op else -1
                
                if free + balance < 0:
                    return False
            
            return balance <= free
        
        return len(s) % 2 == 0 and check(s, locked, '(') and check(s[::-1], locked[::-1], ')') 
            

    
def main():
    sol = Solution()
    print(sol.canBeValid(s = "))()))", locked = "010100"))
    print(sol.canBeValid(s = "()()", locked = "0000"))
    print(sol.canBeValid(s = ")", locked = "0"))

if __name__ == '__main__':
    main()