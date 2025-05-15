from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]] + [words[i] for i in range(1, len(groups)) if groups[i] != groups[i - 1]]

    # def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    #     res = []
    #     prev = ''

    #     for word, bit in zip(words, groups):
    #         if prev != bit:
    #             res.append(word)
    #             prev = bit

    #     return res

        
def main():
    sol = Solution()
    print(sol.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))
    print(sol.getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1]))

if __name__ == '__main__':
    main()