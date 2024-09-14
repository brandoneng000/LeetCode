class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set('aeiou')
        res = 0

        for i in range(n):
            vowel_count = consonant_count = 0

            for j in range(i, n):
                if s[j] in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
                
                if vowel_count == consonant_count and (vowel_count * consonant_count) % k == 0:
                    res += 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.beautifulSubstrings(s = "baeyh", k = 2))
    print(sol.beautifulSubstrings(s = "abba", k = 1))
    print(sol.beautifulSubstrings(s = "bcdf", k = 1))

if __name__ == '__main__':
    main()