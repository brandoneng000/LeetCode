class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        n = len(s)
        count = [0] * 26
        res = []

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        max_count = max(count)

        for i in range(n - 1, -1, -1):
            if count[ord(s[i]) - ord('a')] == max_count:
                count[ord(s[i]) - ord('a')] -= 1
                res.append(s[i])
        
        return ''.join(res[::-1])
        
def main():
    sol = Solution()
    print(sol.lastNonEmptyString("aabcbbca"))
    print(sol.lastNonEmptyString("abcd"))

if __name__ == '__main__':
    main()