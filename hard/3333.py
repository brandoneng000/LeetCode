class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 1_000_000_007
        n = len(word)
        count = 1
        freq = []
        res = 1

        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        for o in freq:
            res = res * o % MOD

        if len(freq) >= k:
            return res

        f = [1] + [0] * (k - 1)
        g = [1] * k

        for i in range(len(freq)):
            f_new = [0] * k

            for j in range(1, k):
                f_new[j] = g[j - 1]

                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % MOD
            g_new = [f_new[0]] + [0] * (k - 1)

            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % MOD
            f, g = f_new, g_new

        return (res - g[k - 1]) % MOD 

        
def main():
    sol = Solution()
    print(sol.possibleStringCount(word = "aabbccdd", k = 7))
    print(sol.possibleStringCount(word = "aabbccdd", k = 8))
    print(sol.possibleStringCount(word = "aaabbb", k = 3))

if __name__ == '__main__':
    main()