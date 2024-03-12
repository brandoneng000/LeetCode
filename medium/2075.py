class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""

        n = len(encodedText)
        res = []
        col = n // rows

        for i in range(col):
            r = 0
            c = i

            while r < rows and c < col:
                res.append(encodedText[r * col + c])
                r += 1
                c += 1
        
        while res[-1] == ' ':
            res.pop()
        
        return "".join(res)

        
def main():
    sol = Solution()
    print(sol.decodeCiphertext(encodedText = "ch   ie   pr", rows = 3))
    print(sol.decodeCiphertext(encodedText = "iveo    eed   l te   olc", rows = 4))
    print(sol.decodeCiphertext(encodedText = "coding", rows = 1))

if __name__ == '__main__':
    main()