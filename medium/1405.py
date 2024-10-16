import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        n = a + b + c
        cur_a = cur_b = cur_c = 0
        res = []

        for _ in range(n):
            if (a >= b and a >= c and cur_a != 2) or (a > 0 and (cur_b == 2 or cur_c == 2)):
                res.append('a')
                a -= 1
                cur_a += 1
                cur_b = 0
                cur_c = 0
            elif (b >= a and b >= c and cur_b != 2) or (b > 0 and (cur_a == 2 or cur_c == 2)):
                res.append('b')
                b -= 1
                cur_b += 1
                cur_a = 0
                cur_c = 0
            elif (c >= a and c >= b and cur_c != 2) or (c > 0 and (cur_a == 2 or cur_b == 2)):
                res.append('c')
                c -= 1
                cur_c += 1
                cur_a = 0
                cur_b = 0
        
        return ''.join(res)


    # def longestDiverseString(self, a: int, b: int, c: int) -> str:
    #     heap = []
    #     res = []
    #     if a > 0:
    #         heapq.heappush(heap, (-a, 'a'))
    #     if b > 0:
    #         heapq.heappush(heap, (-b, 'b'))
    #     if c > 0:
    #         heapq.heappush(heap, (-c, 'c'))

    #     while heap:
    #         count, letter = heapq.heappop(heap)

    #         if res[-2:] == [letter] * 2:
    #             if heap:
    #                 alt_count, alt_letter = heapq.heappop(heap)
    #                 res.append(alt_letter)
    #                 alt_count += 1
    #                 if alt_count != 0:
    #                     heapq.heappush(heap, (alt_count, alt_letter))
    #             else:
    #                 break
            
    #         res.append(letter)
    #         count += 1
    #         if count != 0:
    #             heapq.heappush(heap, (count, letter))
        
    #     return ''.join(res)

def main():
    sol = Solution()
    print(sol.longestDiverseString(a = 1, b = 1, c = 7))
    print(sol.longestDiverseString(a = 7, b = 1, c = 0))

if __name__ == '__main__':
    main()