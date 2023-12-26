class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                res += max(freq) - min(k for k in freq if k)
        
        return res
        
def main():
    sol = Solution()
    print(sol.beautySum("aabcb"))
    print(sol.beautySum("aabcbaa"))

if __name__ == '__main__':
    main()