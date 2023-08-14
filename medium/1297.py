class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cache = { '': 0 }
        n = len(s)

        for i in range(n - minSize + 1):
            cur = s[i: i + minSize]
            if len(set(cur)) > maxLetters:
                continue

            cache[cur] = cache.get(cur, 0) + 1
                
        return max(cache.values())
    
    # def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    #     cache = { '': 0 }
    #     n = len(s)

    #     for size in range(minSize, maxSize + 1):
    #         for i in range(n - size + 1):
    #             cur = s[i: i + size]
    #             if len(set(cur)) > maxLetters:
    #                 continue

    #             cache[cur] = cache.get(cur, 0) + 1
                
    #     return max(cache.values())

def main():
    sol = Solution()
    print(sol.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
    print(sol.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))

if __name__ == '__main__':
    main()