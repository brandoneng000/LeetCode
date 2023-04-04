class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        res = 0

        for index in range(0, len(s), 2):
            res += s[index].count('*')
            
        return res

def main():
    sol = Solution()
    print(sol.countAsterisks("l|*e*et|c**o|*de|"))
    print(sol.countAsterisks("iamprogrammer"))
    print(sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))

if __name__ == '__main__':
    main()