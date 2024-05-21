class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for letter in s:
            if letter == '*':
                res.pop()
            else:
                res.append(letter)
        
        return ''.join(res)
        
def main():
    sol = Solution()
    print(sol.removeStars("leet**cod*e"))
    print(sol.removeStars("erase*****"))

if __name__ == '__main__':
    main()