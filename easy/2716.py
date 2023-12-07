class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
        
def main():
    sol = Solution()
    print(sol.minimizedStringLength("aaabc"))
    print(sol.minimizedStringLength("cbbd"))
    print(sol.minimizedStringLength("dddaaa"))

if __name__ == '__main__':
    main()