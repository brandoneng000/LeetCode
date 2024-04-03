from heapq import heappush, heappop
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        s_count = Counter(s)
        heap = []
        res = []

        for letter in s_count:
            heappush(heap, (-ord(letter), s_count[letter]))


        while heap:
            max_letter, count = heappop(heap)
            res.extend([chr(-max_letter)] * min(repeatLimit, count))
            count = max(0, count - repeatLimit)

            while count and heap:
                temp_letter, temp_count = heappop(heap)
                res.append(chr(-temp_letter))
                temp_count -= 1
                res.extend([chr(-max_letter)] * min(repeatLimit, count))
                count = max(0, count - repeatLimit)
                
                if temp_count > 0:
                    heappush(heap, (temp_letter, temp_count))
            
        return "".join(res)

        
def main():
    sol = Solution()
    print(sol.repeatLimitedString(s = "cczazcc", repeatLimit = 3))
    print(sol.repeatLimitedString(s = "aababab", repeatLimit = 2))

if __name__ == '__main__':
    main()