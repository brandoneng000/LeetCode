class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = list(bin(x)[2:])
        bits = list(bin(n - 1)[2:])

        for i in range(len(res) - 1, -1, -1):
            if res[i] == '0':
                res[i] = bits.pop()
            if not bits:
                break
        
        return int(''.join(bits + res), 2)
        


        
def main():
    sol = Solution()
    print(sol.minEnd(n = 3, x = 4))
    print(sol.minEnd(n = 2, x = 7))

if __name__ == '__main__':
    main()