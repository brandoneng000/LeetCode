class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num: int) -> bool:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    return False
    
            return num != 1
        
        return sum(is_prime(bin(num).count('1')) for num in range(left, right + 1))

def main():
    sol = Solution()
    print(sol.countPrimeSetBits(6, 10))
    print(sol.countPrimeSetBits(10, 15))
    print(sol.countPrimeSetBits(1, 10000))

if __name__ == '__main__':
    main()