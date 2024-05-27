class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        prev = 0
        count = 0
        res = 1

        for letter in s:
            val = ord(letter)
            if val == prev + 1:
                prev += 1
                count += 1
                res = max(res, count)
            else:
                prev = val
                count = 1
        
        return res


        
def main():
    sol = Solution()
    print(sol.longestContinuousSubstring("abacaba"))
    print(sol.longestContinuousSubstring("abcde"))

if __name__ == '__main__':
    main()