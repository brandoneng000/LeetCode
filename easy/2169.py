class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0

        while num1 and num2:
            res += num1 // num2
            num1 %= num2
            num1, num2, = num2, num1
        
        return res

    # def countOperations(self, num1: int, num2: int) -> int:
    #     if not num1 or not num2:
    #         return 0
    #     small = min(num1, num2)
    #     large = max(num1, num2)
    #     res = 0

    #     while large % small != 0:
    #         large -= small
    #         small, large =  min(large, small), max(large, small)
    #         res += 1

    #     return res + large // small


def main():
    sol = Solution()
    print(sol.countOperations(2, 3))
    print(sol.countOperations(10, 10))

if __name__ == '__main__':
    main()