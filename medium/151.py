class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        s = s.split()
        start, end = 0, len(s) - 1
        
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

        return " ".join(s)
        # return " ".join(s.split()[::-1])
        
def main():
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  hello world  "))
    print(sol.reverseWords("a good   example"))

if __name__ == '__main__':
    main()