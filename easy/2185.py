from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


def main():
    sol = Solution()
    print(sol.prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))
    print(sol.prefixCount(words = ["leetcode","win","loops","success"], pref = "code"))

if __name__ == '__main__':
    main()