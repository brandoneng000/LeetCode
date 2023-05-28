from typing import List

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2 and presses == 1:
            return 3
        if n == 2:
            return 4
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8

def main():
    sol = Solution()
    print(sol.flipLights(n = 4, presses = 100))
    print(sol.flipLights(n = 1, presses = 1))
    print(sol.flipLights(n = 2, presses = 1))
    print(sol.flipLights(n = 3, presses = 1))

if __name__ == '__main__':
    main()