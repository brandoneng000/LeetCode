from typing import List
import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1:]

                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)

            res = max(res, dp[word])

        return res

    # def longestStrChain(self, words: List[str]) -> int:
    #     def word_check(pred: str, succ: str):
    #         error = True
    #         index = 0

    #         for letter in succ:
    #             if index < len(pred) and letter == pred[index]:
    #                 index += 1
    #             elif error:
    #                 error = False
    #             else:
    #                 return False

    #         return True
        
    #     def helper(size: int, words: List[str], chain: int):
    #         if not words_size[size]:
    #             return chain

    #         next_valid = []
    #         for word in words:
    #             for pred in words_size[size]:
    #                 if word_check(pred, word):
    #                     next_valid.append(pred)
            
    #         if not next_valid:
    #             return chain
    #         return helper(size - 1, next_valid, chain + 1)

    #     words_size = collections.defaultdict(list)
        
    #     for word in words:
    #         words_size[len(word)].append(word)

    #     res = 1

    #     for size in sorted(words_size.keys(), reverse=True):
    #         res = max(res, helper(size - 1, words_size[size], 1))

    #     return res
    
    # def longestStrChain(self, words: List[str]) -> int:
    #     def word_check(pred: str, succ: str):
    #         error = True
    #         index = 0

    #         for letter in succ:
    #             if index < len(pred) and letter == pred[index]:
    #                 index += 1
    #             elif error:
    #                 error = False
    #             else:
    #                 return False

    #         return True
        
    #     def helper(size: int, words: List[str], chain: int):
    #         if not words_size[size]:
    #             return chain

    #         next_valid = []
    #         for word in words:
    #             for succ in words_size[size]:
    #                 if word_check(word, succ):
    #                     next_valid.append(succ)
            
    #         if not next_valid:
    #             return chain
    #         return helper(size + 1, next_valid, chain + 1)

    #     words_size = collections.defaultdict(list)
        
    #     for word in words:
    #         words_size[len(word)].append(word)

    #     res = 1

    #     for size in sorted(words_size.keys()):
    #         res = max(res, helper(size + 1, words_size[size], 1))

    #     return res


def main():
    sol = Solution()
    print(sol.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
    print(sol.longestStrChain(["a","ab","ac","bd","abc","abd","abdd"]))
    print(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]))
    print(sol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
    print(sol.longestStrChain(["abcd","dbqca"]))

if __name__ == '__main__':
    main()