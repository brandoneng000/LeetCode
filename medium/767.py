import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = collections.Counter(s)
        heap = []
        for letter, count in letters.items():
            heapq.heappush(heap, (-count, letter))
        
        if max(letters.values()) > (len(s) + 1) // 2:
            return ""
        
        res = [''] * len(s)
        index = 0
        while heap:
            count, letter = heapq.heappop(heap)
            count *= -1
            for _ in range(count):
                res[index] = letter
                index += 2
                if index >= len(s):
                    index = 1
        return "".join(res)
        
    # def reorganizeString(self, s: str) -> str:
    #     letters = collections.Counter(s)
    #     hold = None
    #     heap = []

    #     for letter, count in letters.items():
    #         heapq.heappush(heap, (-count, letter))
        
    #     if max(letters.values()) > (len(s) + 1) // 2:
    #         return ""

    #     hold = None
    #     res = ""

    #     while heap:
    #         cur_count, cur_letter = heapq.heappop(heap)
    #         res += cur_letter
    #         if hold is not None and hold[0]:
    #             heapq.heappush(heap, hold)

    #         if cur_count + 1 == 0:
    #             hold = None
    #         else:
    #             hold = (cur_count + 1, cur_letter)

    #     return res




def main():
    sol = Solution()
    print(sol.reorganizeString("aab"))
    print(sol.reorganizeString("aaab"))

if __name__ == '__main__':
    main()