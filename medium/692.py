from typing import List
import heapq
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = collections.Counter(words)
        heap = []
        for word, count in words_count.items():
            heapq.heappush(heap, (-count, word))
        
        return [word[1] for word in heapq.nsmallest(k, heap)]

    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     words_count = {}

    #     for word in words:
    #         words_count[word] = words_count.get(word, 0) + 1
        
    #     words_list = list(set(words))
    #     words_list.sort(key=lambda x: (-words_count[x], x))
    #     return words_list[:k]

def main():
    sol = Solution()
    print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], k = 2))
    print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))

if __name__ == '__main__':
    main()