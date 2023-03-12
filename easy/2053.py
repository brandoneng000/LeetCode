from typing import List
import collections

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_count = collections.Counter(arr)
        
        for word in arr:
            if arr_count[word] == 1:
                k -= 1
                if k == 0:
                    return word
        
        return ""


def main():
    sol = Solution()
    print(sol.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
    print(sol.kthDistinct(arr = ["aaa","aa","a"], k = 1))
    print(sol.kthDistinct(arr = ["a","b","a"], k = 3))

if __name__ == '__main__':
    main()