class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k % 2 == 0 and num % 2 == 1:
            return -1
        if num < k:
            return -1
        
        goal = num % 10

        for i in range(1, 11):
            if k * i % 10 == goal:
                if i * k <= num:
                    return i
        
        return -1
        
def main():
    sol = Solution()
    print(sol.minimumNumbers(num = 58, k = 9))
    print(sol.minimumNumbers(num = 37, k = 2))
    print(sol.minimumNumbers(num = 0, k = 7))

if __name__ == '__main__':
    main()