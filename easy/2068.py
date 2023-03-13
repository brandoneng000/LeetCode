import collections

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_count = collections.Counter(word1)
        word2_count = collections.Counter(word2)
        
        for key in word1_count:
            if abs(word1_count[key] - word2_count.get(key, 0)) > 3:
                return False
        
        for key in word2_count:
            if abs(word2_count[key] - word1_count.get(key, 0)) > 3:
                return False

        return True

def main():
    sol = Solution()
    print(sol.checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))
    print(sol.checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc"))
    print(sol.checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab"))

if __name__ == '__main__':
    main()