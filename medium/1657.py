from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        return Counter(Counter(word1).values()) == Counter(Counter(word2).values())

    # def closeStrings(self, word1: str, word2: str) -> bool:
    #     if len(word1) != len(word2):
    #         return False
        
    #     if set(word1) != set(word2):
    #         return False
        
    #     count_word1 = Counter(word1)
    #     count_word2 = Counter(word2)
    #     needed = []
    #     stock = []

    #     for letter in set(word1):
    #         if count_word1[letter] != count_word2[letter]:
    #             stock.append(count_word1[letter])
    #             needed.append(count_word2[letter])

    #     for val in needed:
    #         for i in range(len(stock)):
    #             if stock[i] == val:
    #                 stock[i] = -1
    #                 break
    #         else:
    #             return False
        
    #     return True
        
        
def main():
    sol = Solution()
    print(sol.closeStrings(word1 = "abc", word2 = "bca"))
    print(sol.closeStrings(word1 = "a", word2 = "aa"))
    print(sol.closeStrings(word1 = "cabbba", word2 = "abbccc"))

if __name__ == '__main__':
    main()