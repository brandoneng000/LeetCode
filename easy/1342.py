class Solution:
    def numberOfSteps(self, num: int) -> int:
        # result = 0

        # while num:
        #     if num % 2:
        #         num -= 1
        #     else:
        #         num //= 2
        #     result += 1

        # return result
        if not num:
            return 0
        
        result = 0

        while num:
            result += 2 if num % 2 else 1
            num >>= 1

        return result - 1

def main():
    sol = Solution()
    print(sol.numberOfSteps(14))
    print(sol.numberOfSteps(15))
    print(sol.numberOfSteps(8))
    print(sol.numberOfSteps(123))

if __name__ == '__main__':
    main()