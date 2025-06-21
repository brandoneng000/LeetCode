from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        letter_count = Counter(word)
        res = float('inf')

        for a in letter_count.values():
            cur = 0

            for b in letter_count.values():
                if a > b:
                    cur += b
                elif b > a + k:
                    cur += b - a - k
            
            res = min(res, cur)
        
        return res
    
    # def minimumDeletions(self, word: str, k: int) -> int:
    #     letter_count = Counter(word)
    #     res = float('inf')

    #     for a in letter_count:
    #         cur = 0

    #         for b in letter_count:
    #             if letter_count[a] > letter_count[b]:
    #                 cur += letter_count[b]
    #             else:
    #                 cur += max(0, letter_count[b] - letter_count[a] - k)
            
    #         res = min(res, cur)
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.minimumDeletions(word = "aabcaba", k = 0))
    print(sol.minimumDeletions(word = "dabdcbdcdcd", k = 2))
    print(sol.minimumDeletions(word = "aaabaaa", k = 2))

if __name__ == '__main__':
    main()