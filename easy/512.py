class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))

        return max(len(a), len(b)) if a != b else -1
        
def main():
    sol = Solution()
    print(sol.findLUSlength("aba", "cdc"))
    print(sol.findLUSlength("abcde", "abcdg"))

if __name__ == '__main__':
    main()