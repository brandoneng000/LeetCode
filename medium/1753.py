from heapq import heappush, heappop

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = []
        res = 0

        heappush(heap, -a)
        heappush(heap, -b)
        heappush(heap, -c)

        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            x += 1
            y += 1

            if x < 0:
                heappush(heap, x)
            
            if y < 0:
                heappush(heap, y)

            res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumScore(a = 2, b = 4, c = 6))
    print(sol.maximumScore(a = 4, b = 4, c = 6))
    print(sol.maximumScore(a = 1, b = 8, c = 8))

if __name__ == '__main__':
    main()