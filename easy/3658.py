from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = even = 0
        num = 1

        for _ in range(n):
            odd += num
            even += num + 1
            num += 2
        
        return gcd(odd, even)

        
def main():
    sol = Solution()
    print(sol.gcdOfOddEvenSums(999))
    print(sol.gcdOfOddEvenSums(4))
    print(sol.gcdOfOddEvenSums(5))

if __name__ == '__main__':
    main()