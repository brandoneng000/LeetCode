class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        num_set = set()
        
        while (total != 1):
            total = 0
            while n > 0:
                digit = n % 10
                n //= 10
                digit *= digit
                total += digit
            if total in num_set:
                return False
            num_set.add(total)
            n = total

        return True

def main():
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(2))

if __name__ == '__main__':
    main()