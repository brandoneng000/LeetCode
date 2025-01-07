from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sentence = ' '.join(words)
        res = []

        for word in words:
            if sentence.count(word) > 1:
                res.append(word)
        
        return res


    # def stringMatching(self, words: List[str]) -> List[str]:
    #     words.sort(key=len, reverse=True)
    #     words_set = set()
    #     res = []

    #     for word in words:
            
    #         for large_word in words_set:
    #             if word in large_word:
    #                 res.append(word)
    #                 break
    #         else:
    #             words_set.add(word)
        
    #     return res


    # def stringMatching(self, words: List[str]) -> List[str]:
    #     words.sort(key=len)
    #     res = []
        
    #     for index, word in enumerate(words):
    #         largest = len(words) - 1
    #         while index < largest:
    #             if word in words[largest]:
    #                 res.append(word)
    #                 break
    #             else:
    #                 largest -= 1

    #     return res

def main():
    sol = Solution()
    print(sol.stringMatching(["mass","as","hero","superhero"]))
    print(sol.stringMatching(["leetcode","et","code"]))
    print(sol.stringMatching(["blue","green","bu"]))

if __name__ == '__main__':
    main()