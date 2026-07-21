class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        res = s.count('1')

        zero_block = []
        i = 0

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if s[start] == '0':
                zero_block.append(i - start)
        
        m = len(zero_block)

        if m < 2:
            return res

        delta = 0

        for i in range(m - 1):
            delta = max(delta, zero_block[i] + zero_block[i + 1])
        
        return res + delta
        
def main():
    sol = Solution()
    print(sol.maxActiveSectionsAfterTrade("01"))
    print(sol.maxActiveSectionsAfterTrade("0100"))
    print(sol.maxActiveSectionsAfterTrade("1000100"))
    print(sol.maxActiveSectionsAfterTrade("01010"))

if __name__ == '__main__':
    main()