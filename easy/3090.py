class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        count = [0] * 26
        left = 0
        res = 0

        for right in range(n):
            index = ord(s[right]) - ord('a')
            count[index] += 1

            while left < right and count[index] > 2:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumLengthSubstring("bcbbbcba"))
    print(sol.maximumLengthSubstring("aaaa"))

if __name__ == '__main__':
    main()