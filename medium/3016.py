from collections import Counter
from heapq import heappush, heappop

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        sorted_cnt = sorted(cnt.values(), reverse=True)
        res = 0

        for i, f in enumerate(sorted_cnt):
            row = i // 8 + 1
            res += f * row

        return res

    # def minimumPushes(self, word: str) -> int:
    #     count = Counter(word)
    #     heap = []

    #     for i in range(2, 10):
    #         heappush(heap, (0, 0, i))
        
    #     for letter, c in count.most_common():
    #         letter_count, presses, num = heappop(heap)
    #         letter_count += 1
    #         presses += letter_count * c
    #         heappush(heap, (letter_count, presses, num))
        
    #     return sum(presses for letter_count, presses, num in heap)
        
def main():
    sol = Solution()
    print(sol.minimumPushes("ajqjtbjhczpakocxjrsugawef"))
    print(sol.minimumPushes("abcde"))
    print(sol.minimumPushes("xyzxyzxyzxyz"))
    print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))

if __name__ == '__main__':
    main()