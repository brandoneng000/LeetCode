class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        j = 0

        for letter in s:
            if j < n and letter == t[j]:
                j += 1
        
        return n - j
        
def main():
    sol = Solution()
    print(sol.appendCharacters(s = "coaching", t = "coding"))
    print(sol.appendCharacters(s = "abcde", t = "a"))
    print(sol.appendCharacters(s = "z", t = "abcde"))

if __name__ == '__main__':
    main()