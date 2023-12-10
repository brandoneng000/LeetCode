from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cache = set()
        res = 0

        for word in words:
            if word in cache:
                res += 1
            else:
                cache.add(word[::-1])
            
        return res
        
def main():
    sol = Solution()
    print(sol.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
    print(sol.maximumNumberOfStringPairs(["ab","ba","cc"]))
    print(sol.maximumNumberOfStringPairs(["aa","ab"]))

if __name__ == '__main__':
    main()