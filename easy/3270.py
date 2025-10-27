class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)
        res = []

        for i in range(4):
            res.append(min(num1[i], num2[i], num3[i]))
        
        return int(''.join(res))

        
def main():
    sol = Solution()
    print(sol.generateKey(num1 = 1, num2 = 10, num3 = 1000))
    print(sol.generateKey(num1 = 987, num2 = 879, num3 = 798))
    print(sol.generateKey(num1 = 1, num2 = 2, num3 = 3))

if __name__ == '__main__':
    main()