class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        letter_count = Counter(s)
        return len(set(letter_count.values())) == 1

def main():
    sol = Solution()
    print(sol.areOccurrencesEqual("abacbc"))
    print(sol.areOccurrencesEqual("aaabb"))

if __name__ == '__main__':
    main()