class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = bin(n)[2:]
        m = len(binary)
        res = 0
        sign = 1

        for i in range(m):
            bit = binary[i]
            if bit == '1':
                res += sign * (2 ** (m - i) - 1)
                sign *= -1
        
        return res

    # def minimumOneBitOperations(self, n: int) -> int:
    #     if n == 0:
    #         return 0
        
    #     k = 0
    #     cur = 1
        
    #     while (cur * 2) <= n:
    #         cur *= 2
    #         k += 1
        
    #     return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ cur)
        
def main():
    sol = Solution()
    print(sol.minimumOneBitOperations(3))
    print(sol.minimumOneBitOperations(6))

if __name__ == '__main__':
    main()