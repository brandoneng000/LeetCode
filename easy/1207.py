from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        arr_count = Counter(arr)
        return len(arr_count.values()) == len(set(arr_count.values()))

def main():
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))
    print(sol.uniqueOccurrences([1,2]))
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))

if __name__ == '__main__':
    main()