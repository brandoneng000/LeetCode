class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.helper(n)

    def helper(self, n: int): 
        if n == 1:
            return 0
        elif n % 2:
            return min(self.helper(n + 1) + 1, self.helper(n - 1) + 1)
        else:
            return self.helper(n // 2) + 1
    # def integerReplacement(self, n: int) -> int:
    #     res = 0

    #     while n != 1:
    #         if n % 2 == 0:
    #             n //= 2
    #         elif n % 4 == 1 or n == 3:
    #             n -= 1
    #         else:
    #             n += 1

    #         res += 1
        
    #     return res


def main():
    sol = Solution()
    print(sol.integerReplacement(8))
    print(sol.integerReplacement(7))
    print(sol.integerReplacement(4))

if __name__ == '__main__':
    main()