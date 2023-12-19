from collections import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        count_a = Counter(ord(c) - 97 for c in a)
        count_b = Counter(ord(c) - 97 for c in b)
        res = m + n - max((count_a + count_b).values())

        for i in range(25):
            count_a[i + 1] += count_a[i]
            count_b[i + 1] += count_b[i]
            res = min(res, m - count_a[i] + count_b[i])
            res = min(res, n - count_b[i] + count_a[i])
        
        return res

        
def main():
    sol = Solution()
    print(sol.minCharacters(a = "aba", b = "caa"))
    print(sol.minCharacters(a = "dabadd", b = "cda"))

if __name__ == '__main__':
    main()