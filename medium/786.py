from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i, val in enumerate(arr):
            heapq.heappush(heap, (1 / val, i, 0, 1, val))

        while k > 0:
            v, row, col, p, q = heapq.heappop(heap)

            if col < len(arr) and row > col + 1:
                heapq.heappush(heap, (arr[col + 1] / arr[row], row, col + 1, arr[col + 1], arr[row]))
            k -= 1

        return [p, q]


    # def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    #     fractions = []
    #     for i in range(len(arr)):
    #         for j in range(len(arr) - 1, i, -1):
    #             fractions.append((arr[i] / arr[j], arr[i], arr[j]))
        
    #     fractions.sort()
    #     # print(fractions)
    #     return [fractions[k - 1][1], fractions[k - 1][2]]


def main():
    sol = Solution()
    print(sol.kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))
    print(sol.kthSmallestPrimeFraction(arr = [1,7], k = 1))

if __name__ == '__main__':
    main()