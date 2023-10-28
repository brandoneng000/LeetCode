class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 1000000007
        cur_vowels = { 'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1 }

        for _ in range(n - 1):
            next_vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }

            for prev in cur_vowels:
                if prev == 'a':
                    next_vowels['e'] += cur_vowels[prev]
                elif prev == 'e':
                    next_vowels['a'] += cur_vowels[prev]
                    next_vowels['i'] += cur_vowels[prev]
                elif prev == 'i':
                    next_vowels['a'] += cur_vowels[prev]
                    next_vowels['e'] += cur_vowels[prev]
                    next_vowels['o'] += cur_vowels[prev]
                    next_vowels['u'] += cur_vowels[prev]
                elif prev == 'o':
                    next_vowels['i'] += cur_vowels[prev]
                    next_vowels['u'] += cur_vowels[prev]
                elif prev == 'u':
                    next_vowels['a'] += cur_vowels[prev]

            cur_vowels = next_vowels

        return sum(cur_vowels.values()) % mod

        
def main():
    sol = Solution()
    print(sol.countVowelPermutation(1))
    print(sol.countVowelPermutation(2))
    print(sol.countVowelPermutation(5))

if __name__ == '__main__':
    main()