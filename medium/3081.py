from typing import List
from heapq import heappush, heappop
from collections import Counter, deque
from string import ascii_lowercase

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        n = len(s)
        replacement = []
        count = Counter(s)
        res = list(s)
        heap = []

        for c in ascii_lowercase:
            heappush(heap, (count[c], c))
        
        for _ in range(count['?']):
            freq, c = heappop(heap)
            replacement.append(c)
            heappush(heap, (freq + 1, c))
        
        replacement = deque(sorted(replacement))

        for i in range(n):
            if res[i] == '?':
                res[i] = replacement.popleft()

        return ''.join(res)

        
def main():
    sol = Solution()
    print(sol.minimizeStringValue("???"))
    print(sol.minimizeStringValue("a?a?"))

if __name__ == '__main__':
    main()