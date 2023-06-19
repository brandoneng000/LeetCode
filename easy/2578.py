class Solution:
    def splitNum(self, num: int) -> int:
        n = sorted(str(num))
        return int("".join(n[::2])) + int("".join(n[1::2]))

    # def splitNum(self, num: int) -> int:
    #     n = sorted(str(num))
    #     num1, num2 = [], []

    #     for i in range(0, len(n), 2):
    #         num1.append(n[i])
        
    #     for i in range(1, len(n), 2):
    #         num2.append(n[i])
        
    #     return int("".join(num1)) + int("".join(num2))
        
        

def main():
    sol = Solution()
    print(sol.splitNum(4325))
    print(sol.splitNum(687))

if __name__ == '__main__':
    main()