class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        letter_count = {}
        res = 0
        freq = 0

        for index in range(len(s)):
            letter_count[s[index]] = letter_count.get(s[index], 0) + 1

            freq = max(freq, letter_count[s[index]])
            is_valid = (index + 1 - start - freq <= k)
            if not is_valid:
                letter_count[s[start]] -= 1
                start += 1

            res = index + 1 - start
        
        return res

        
def main():
    sol = Solution()
    print(sol.characterReplacement(s = "ABAB", k = 2))
    print(sol.characterReplacement(s = "AABABBA", k = 1))
    print(sol.characterReplacement(s = "ABBB", k = 2))

if __name__ == '__main__':
    main()