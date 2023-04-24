from typing import List
import collections

class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_count = collections.defaultdict(list)

        def helper(word: str):
            prev = word[0]
            diff_array = []
            for index in range(1, len(word)):
                diff_array.append(ord(prev) - ord(word[index]))
            return tuple(diff_array)
        
        for index, word in enumerate(words):
            diff_count[helper(word)].append(word)
            if len(diff_count) > 1 and index > 2:
                break
        
        for diff in diff_count:
            if len(diff_count[diff]) == 1:
                return diff_count[diff][0]


def main():
    sol = Solution()
    print(sol.oddString(words = ["adc","wzy","abc"]))
    print(sol.oddString(words = ["aaa","bob","ccc","ddd"]))

if __name__ == '__main__':
    main()