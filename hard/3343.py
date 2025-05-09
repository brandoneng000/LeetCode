from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 1000000007
        n = len(num)
        total = 0
        count = [0] * 10

        for d in num:
            digit = int(d)
            count[digit] += 1
            total += digit
        
        if total % 2 == 1:
            return 0

        target = total // 2
        max_odd = (n + 1) // 2
        dp = [[0] * (max_odd + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        psum = total_sum = 0

        for i in range(10):
            psum += count[i]
            total_sum += i * count[i]

            for odd_count in range(min(psum, max_odd), max(0, psum - (n - max_odd)) - 1, -1):
                even_count = psum - odd_count

                for cur in range(min(total_sum, target), max(0, total_sum - target) - 1, -1):
                    res = 0

                    for j in range(max(0, count[i] - even_count), min(count[i], odd_count) + 1):
                        if i * j > cur:
                            break
                        ways = comb(odd_count, j) * comb(even_count, count[i] - j) % mod
                        res = (res + ways * dp[cur - i * j][odd_count - j] % mod) % mod
                        dp[cur][odd_count] = res % mod

        return dp[target][max_odd]
        
def main():
    sol = Solution()
    print(sol.countBalancedPermutations("123"))
    print(sol.countBalancedPermutations("112"))
    print(sol.countBalancedPermutations("12345"))

if __name__ == '__main__':
    main()