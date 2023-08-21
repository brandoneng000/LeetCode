class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0

        while a or b or c:
            if c & 1 == (a | b) & 1:
                pass
            else:
                if c & 1 == 1:
                    res += 1
                else:
                    res += (a & 1) + (b & 1)

            c >>= 1
            b >>= 1
            a >>= 1
        
        return res

def main():
    sol = Solution()
    print(sol.minFlips(a = 2, b = 6, c = 5))
    print(sol.minFlips(a = 4, b = 2, c = 7))
    print(sol.minFlips(a = 1, b = 2, c = 3))

if __name__ == '__main__':
    main()