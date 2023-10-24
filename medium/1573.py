class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        mod = 1000000007
        ones = s.count('1')

        if ones % 3 != 0:
            return 0
        if ones == 0:
            return (n - 2) * (n - 1) // 2 % mod

        req_ones = ones // 3
        prefix = [0] * n
        prefix[0] = 1 if s[0] == '1' else 0
        count = left = right = 0

        for bit in s:
            if bit == '1':
                count += 1
            
            if count == req_ones:
                left += 1
            elif count == 2 * req_ones:
                right += 1
        
        return left * right % mod
                
        
def main():
    sol = Solution()
    print(sol.numWays("10101"))
    print(sol.numWays("1001"))
    print(sol.numWays("0000"))

if __name__ == '__main__':
    main()