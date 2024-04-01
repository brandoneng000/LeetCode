class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n - 1, -1, -1):
            if s[i] != ' ':
                res += 1
            
            if s[i] == ' ' and res != 0:
                break
        
        return res

    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(s.split()[-1])
        

def main():
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord("luffy is still joyboy"))

if __name__ == '__main__':
    main()