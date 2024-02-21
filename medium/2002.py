class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindrome = {}

        for mask in range(1, 1 << n):
            subseq = []

            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])
            if subseq == subseq[::-1]:
                palindrome[mask] = len(subseq)
        
        res = 0
        for mask1, length1 in palindrome.items():
            for mask2, length2 in palindrome.items():
                if mask1 & mask2 == 0:
                    res = max(res, length1 * length2)
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxProduct("leetcodecom"))
    print(sol.maxProduct("bb"))
    print(sol.maxProduct("accbcaxxcxx"))

if __name__ == '__main__':
    main()