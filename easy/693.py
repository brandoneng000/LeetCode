class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0

    # def hasAlternatingBits(self, n: int) -> bool:
    #     odd = n % 2 == 1

    #     while n:
    #         n >>= 1
    #         if odd:
    #             odd = n % 2 == 1
    #             if odd:
    #                 return False
    #         else:
    #             odd = n % 2 == 1
    #             if not odd:
    #                 return False

    #     return True 
    
    # def hasAlternatingBits(self, n: int) -> bool:
    #     n, current = divmod(n, 2)
    #     while n:
    #         if current == n % 2:
    #             return False
    #         n, current = divmod(n, 2)
        
    #     return True

def main():
    sol = Solution()
    print(sol.hasAlternatingBits(5))
    print(sol.hasAlternatingBits(7))
    print(sol.hasAlternatingBits(11))

if __name__ == '__main__':
    main()