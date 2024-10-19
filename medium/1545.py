class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip = 0
        l = 2 ** n - 1

        while k > 1:
            if k == l // 2 + 1:
                return str(1 ^ flip)

            if k > l // 2:
                k = l + 1 - k
                flip = 1 - flip
            
            l //= 2
        
        return str(flip)


    # def findKthBit(self, n: int, k: int) -> str:
    #     s = '0'

    #     for _ in range(n):
    #         invert = "".join('0' if bit == '1' else '1' for bit in s[::-1])
    #         s = s + '1' + invert

    #         if len(s) > k + 1:
    #             break
        
    #     return s[k - 1]
        
def main():
    sol = Solution()
    print(sol.findKthBit(n = 10, k = 1))
    print(sol.findKthBit(n = 3, k = 1))
    print(sol.findKthBit(n = 4, k = 11))

if __name__ == '__main__':
    main()