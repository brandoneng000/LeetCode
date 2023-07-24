from string import ascii_lowercase

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letter_graph = { c: [i // 5, i % 5] for i, c in enumerate(ascii_lowercase) }
        x0, y0 = 0, 0
        res = []

        for letter in target:
            x, y = letter_graph[letter]
            if y < y0:
                res.append('L' * (y0 - y))
            if x < x0:
                res.append('U' * (x0 - x))
            if x > x0:
                res.append('D' * (x - x0))
            if y > y0:
                res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        
        return "".join(res)
        
                

def main():
    sol = Solution()
    print(sol.alphabetBoardPath("leet"))
    print(sol.alphabetBoardPath("code"))

if __name__ == '__main__':
    main()