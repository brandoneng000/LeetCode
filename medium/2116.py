class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n % 2:
            return False
        
        open_brackets = []
        free = []

        for i in range(n):
            if locked[i] == '0':
                free.append(i)
            elif s[i] == '(':
                open_brackets.append(i)
            elif s[i] == ')':
                if open_brackets:
                    open_brackets.pop()
                elif free:
                    free.pop()
                else:
                    return False
                
        while open_brackets and free and open_brackets[-1] < free[-1]:
            open_brackets.pop()
            free.pop()
        
        return not bool(open_brackets)


    # def canBeValid(self, s: str, locked: str) -> bool:
    #     def check(s: str, locked: str, op: str):
    #         free = 0
    #         balance = 0

    #         for i in range(len(s)):
    #             if locked[i] == '0':
    #                 free += 1
    #             else:
    #                 balance += 1 if s[i] == op else -1
                
    #             if free + balance < 0:
    #                 return False
            
    #         return balance <= free
        
    #     return len(s) % 2 == 0 and check(s, locked, '(') and check(s[::-1], locked[::-1], ')') 
            

    
def main():
    sol = Solution()
    print(sol.canBeValid(s = "))()))", locked = "010100"))
    print(sol.canBeValid(s = "()()", locked = "0000"))
    print(sol.canBeValid(s = ")", locked = "0"))

if __name__ == '__main__':
    main()