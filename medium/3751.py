class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def helper(num: str):
            n = len(num)
            total = 0

            for i in range(1, n - 1):
                if num[i - 1] < num[i] > num[i + 1] or num[i - 1] > num[i] < num[i + 1]:
                    total += 1
            
            return total
        
        res = 0

        for num in range(num1, num2 + 1):
            res += helper(str(num))

        return res

def main():
    sol = Solution()
    print(sol.totalWaviness(num1 = 120, num2 = 130))
    print(sol.totalWaviness(num1 = 198, num2 = 202))
    print(sol.totalWaviness(num1 = 4848, num2 = 4848))

if __name__ == '__main__':
    main()