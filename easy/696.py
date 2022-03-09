class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        cur = 1
        count = 0

        for index in range(1, len(s)):
            test1 = s[index-1]
            test2 = s[index]
            if s[index-1] != s[index]:
                count += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return count + min(prev, cur)

        
def main():
    sol = Solution()
    print(sol.countBinarySubstrings("00110011"))

if __name__ == '__main__':
    main()