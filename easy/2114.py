from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return len(max(sentences, key=lambda x: len(x.split())).split())

def main():
    sol = Solution()
    print(sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
    print(sol.mostWordsFound(["please wait", "continue to fight", "continue to win"]))
    print(sol.mostWordsFound(["duck duck duck duck duck duck duck duck duck duck duck duck", "continue to fight", "continue to win"]))

if __name__ == '__main__':
    main()