from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []
        
        for index, word in enumerate(words):
            largest = len(words) - 1
            while index < largest:
                if word in words[largest]:
                    res.append(word)
                    break
                else:
                    largest -= 1

        return res

def main():
    sol = Solution()
    print(sol.stringMatching(["mass","as","hero","superhero"]))
    print(sol.stringMatching(["leetcode","et","code"]))
    print(sol.stringMatching(["blue","green","bu"]))

if __name__ == '__main__':
    main()