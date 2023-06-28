from typing import List

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = 0
        res = 0

        for n in s:
            if n == '0':
                zero += 1

        res = zero

        for n in s:
            if n == '0':
                zero -= 1
                res = min(res, zero)
            else:
                zero += 1
        
        return res

def main():
    sol = Solution()
    print(sol.minFlipsMonoIncr("00110"))
    print(sol.minFlipsMonoIncr("010110"))
    print(sol.minFlipsMonoIncr("00011000"))

if __name__ == '__main__':
    main()