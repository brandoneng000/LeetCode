from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        for left in range(n):
            count = Counter()

            for right in range(left, n):
                letter = s[right]
                count[letter] += 1

                if count[letter] == k:
                    res += n - right
                    break
        
        return res

        
def main():
    sol = Solution()
    print(sol.numberOfSubstrings(s = "abacb", k = 2))
    print(sol.numberOfSubstrings(s = "abcde", k = 1))

if __name__ == '__main__':
    main()