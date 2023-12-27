class Solution:
    def finalString(self, s: str) -> str:
        res = []

        for letter in s:
            if letter == 'i':
                res = res[::-1]
            else:
                res.append(letter)
        
        return "".join(res)
        
def main():
    sol = Solution()
    print(sol.finalString("string"))
    print(sol.finalString("poiinter"))

if __name__ == '__main__':
    main()