from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd_max = 0
        even_min = float('inf')

        for letter in count:
            if count[letter] % 2:
                odd_max = max(odd_max, count[letter])
            else:
                even_min = min(even_min, count[letter])
        
        return odd_max - even_min

        
def main():
    sol = Solution()
    print(sol.maxDifference("aaaaabbc"))
    print(sol.maxDifference("abcabcab"))

if __name__ == '__main__':
    main()