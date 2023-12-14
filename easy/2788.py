from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for word in words:
            for s in word.split(separator):
                if s:
                    res.append(s)
        
        return res
        
def main():
    sol = Solution()
    print(sol.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
    print(sol.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
    print(sol.splitWordsBySeparator(words = ["|||"], separator = "|"))

if __name__ == '__main__':
    main()