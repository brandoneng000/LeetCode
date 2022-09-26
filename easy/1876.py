class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0

        for index in range(len(s) - 2):
            if len(set(s[index: index + 3])) == 3:
                result += 1

        return result
        
def main():
    sol = Solution()
    print(sol.countGoodSubstrings("xyzzaz"))
    print(sol.countGoodSubstrings("aababcabc"))

if __name__ == '__main__':
    main()