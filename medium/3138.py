from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        count = Counter()
        res = n

        for i in range(n // 2):
            count[s[i]] += 1

            if n % (i + 1) == 0:
                for j in range(i + 1, n, i + 1):
                    temp = Counter(s[j: j + i + 1])
                    if count != temp:
                        break
                else:
                    return i + 1

        return res

        
def main():
    sol = Solution()
    print(sol.minAnagramLength("aabbabab"))
    print(sol.minAnagramLength("abba"))
    print(sol.minAnagramLength("cdef"))

if __name__ == '__main__':
    main()