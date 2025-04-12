from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]

            palindromic_int = int(s)

            if palindromic_int % k == 0:
                sorted_str = ''.join(sorted(s))
                dictionary.add(sorted_str)
        
        fac = [factorial(i) for i in range(n + 1)]
        res = 0

        for s in dictionary:
            count = [0] * 10

            for digit in s:
                count[int(digit)] += 1

            total = (n - count[0]) * fac[n - 1]

            for x in count:
                total //= fac[x]

            res += total
        
        return res

        
def main():
    sol = Solution()
    print(sol.countGoodIntegers(n = 3, k = 5))
    print(sol.countGoodIntegers(n = 1, k = 4))
    print(sol.countGoodIntegers(n = 5, k = 6))

if __name__ == '__main__':
    main()