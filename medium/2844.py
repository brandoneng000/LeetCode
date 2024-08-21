class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        five = False
        zero = False
        zero_count = 0

        for i in range(n - 1, -1, -1):
            if five and (num[i] == '2' or num[i] == '7'):
                return n - i - 2
            
            if zero and (num[i] == '0' or num[i] == '5'):
                return n - i - 2

            if not five and num[i] == '5':
                five = True
            if not zero and num[i] == '0':
                zero = True
            
            if num[i] == '0':
                zero_count += 1

        return n - zero_count
        
def main():
    sol = Solution()
    print(sol.minimumOperations("2245047"))
    print(sol.minimumOperations("2908305"))
    print(sol.minimumOperations("10"))

if __name__ == '__main__':
    main()