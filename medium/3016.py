from collections import Counter
from heapq import heappush, heappop

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        heap = []

        for i in range(2, 10):
            heappush(heap, (0, 0, i))
        
        for letter, c in count.most_common():
            letter_count, presses, num = heappop(heap)
            letter_count += 1
            presses += letter_count * c
            heappush(heap, (letter_count, presses, num))
        
        return sum(presses for letter_count, presses, num in heap)
        
def main():
    sol = Solution()
    print(sol.minimumPushes("ajqjtbjhczpakocxjrsugawef"))
    print(sol.minimumPushes("abcde"))
    print(sol.minimumPushes("xyzxyzxyzxyz"))
    print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))

if __name__ == '__main__':
    main()