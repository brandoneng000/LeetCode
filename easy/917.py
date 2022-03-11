class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            while start < len(s) and not s[start].isalpha():
                start += 1
            while end >= 0 and not s[end].isalpha():
                end -= 1
            if start >= end:
                break
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

        return "".join(s)

        
def main():
    sol = Solution()
    print(sol.reverseOnlyLetters("ab-cd"))
    print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))

if __name__ == '__main__':
    main()