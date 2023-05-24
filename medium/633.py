import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            temp = math.sqrt(c - i * i)
            if temp == int(temp):
                return True
        return False
    
    # def judgeSquareSum(self, c: int) -> bool:
    #     sum_diff = set()

    #     for i in range(int(math.sqrt(c)) + 1):
    #         temp = math.pow(i, 2)
    #         if temp > c:
    #             break
    #         sum_diff.add(c - temp)
        
    #     for i in range(int(math.sqrt(c)) + 1):
    #         if math.pow(i, 2) in sum_diff:
    #             return True
        
    #     return False

def main():
    sol = Solution()
    print(sol.judgeSquareSum(1 << 30))
    print(sol.judgeSquareSum(5))
    print(sol.judgeSquareSum(3))

if __name__ == '__main__':
    main()