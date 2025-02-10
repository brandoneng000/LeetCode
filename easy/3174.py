class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for letter in s:
            if letter.isdigit():
                res.pop()
            else:
                res.append(letter)

        return ''.join(res)
        
def main():
    sol = Solution()
    print(sol.clearDigits("abc"))
    print(sol.clearDigits("cb34"))

if __name__ == '__main__':
    main()