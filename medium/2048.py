from itertools import permutations
from bisect import bisect_right

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        nums = [1, 22, 122, 333, 1333, 4444, 44441, 55555, 22333, 122333, 155555, 224444, 666666]
        nums = [str(num) for num in nums]
        candidates = []

        for num in nums:
            candidates += list(set("".join(p) for p in permutations(list(num))))
        
        candidates = [int(c) for c in candidates]
        candidates.append(1224444)
        candidates.sort()
        index = bisect_right(candidates, n)
        return candidates[index]
        
def main():
    sol = Solution()
    print(sol.nextBeautifulNumber(1))
    print(sol.nextBeautifulNumber(1000))
    print(sol.nextBeautifulNumber(3000))

if __name__ == '__main__':
    main()