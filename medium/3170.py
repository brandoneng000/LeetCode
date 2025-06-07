from heapq import heappush, heappop
from string import ascii_lowercase
from collections import defaultdict

class Solution:
    def clearStars(self, s: str) -> str:
        res = list(s)
        heap = []

        for i, c in enumerate(s):
            if c == '*':
                res[i] = ''
                char, index = heappop(heap)
                res[-index] = ''
            else:
                heappush(heap, (c, -i))
        
        return ''.join(res)

    # def clearStars(self, s: str) -> str:
    #     indexes = defaultdict(list)
    #     res = list(s)

    #     for i, letter in enumerate(s):
    #         if letter == '*':
    #             res[i] = ''
    #             cur = min(indexes)
    #             res[indexes[cur].pop()] = ''
                
    #             if not indexes[cur]:
    #                 indexes.pop(cur)
    #         else:
    #             indexes[letter].append(i)
        
    #     return ''.join(res)


def main():
    sol = Solution()
    print(sol.clearStars("aaba*"))
    print(sol.clearStars("abc"))

if __name__ == '__main__':
    main()