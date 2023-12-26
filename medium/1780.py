class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 != 2:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
        
        return n == 1

    # def checkPowersOfThree(self, n: int) -> bool:
    #     powers_three = [3 ** i for i in range(15)]
        
    #     def helper(cur: int, index: int):
    #         for i in range(index, len(powers_three)):
    #             if cur + powers_three[i] > n:
    #                 return False
    #             elif cur + powers_three[i] == n:
    #                 return True
    #             else:
    #                 if helper(cur + powers_three[i], i + 1):
    #                     return True
    #         return False
        
    #     for i in range(len(powers_three)):
    #         if powers_three[i] < n:
    #             if helper(powers_three[i], i + 1):
    #                 return True
    #         elif powers_three[i] == n:
    #             return True
        
    #     return False
        
def main():
    sol = Solution()
    print(sol.checkPowersOfThree(12))
    print(sol.checkPowersOfThree(91))
    print(sol.checkPowersOfThree(21))

if __name__ == '__main__':
    main()