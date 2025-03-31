from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        numbers = 8
        pressses = 1
        res = 0

        for letter, c in count.most_common():
            res += pressses * c
            numbers -= 1

            if numbers == 0:
                pressses += 1
                numbers = 8
        
        return res
            

        
def main():
    sol = Solution()
    print(sol.minimumPushes("abcde"))
    print(sol.minimumPushes("xycdefghij"))

if __name__ == '__main__':
    main()