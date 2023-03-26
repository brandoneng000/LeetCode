from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for letter in range(ord(s[0]), ord(s[3]) + 1):
            for num in range(int(s[1]), int(s[4]) + 1):
                res.append(chr(letter) + str(num))

        return res

def main():
    sol = Solution()
    print(sol.cellsInRange("K1:L2"))
    print(sol.cellsInRange("A1:F1"))

if __name__ == '__main__':
    main()