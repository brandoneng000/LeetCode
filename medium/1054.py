from typing import List
import collections
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        res = [None] * n
        barcode_count = collections.Counter(barcodes)
        index = 0

        for code, count in barcode_count.most_common():
            for _ in range(count):
                if index >= n:
                    index = 1
                res[index] = code
                index += 2
        
        return res

    # def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    #     res = [None] * len(barcodes)
    #     barcode_count = collections.Counter(barcodes)
    #     heap = []
        
    #     for key in barcode_count:
    #         heapq.heappush(heap, (-barcode_count[key], key))
        
    #     index = 0
    #     while heap:
    #         count, key = heapq.heappop(heap)
    #         count = -count

    #         while count:
    #             if index >= len(barcodes):
    #                 index = 1
    #             res[index] = key
    #             index += 2
    #             count -= 1
            
    #     return res


def main():
    sol = Solution()
    print(sol.rearrangeBarcodes([1,1,1,2,2,2]))
    print(sol.rearrangeBarcodes([1,1,1,1,2,2,3,3]))

if __name__ == '__main__':
    main()