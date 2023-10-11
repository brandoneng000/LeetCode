from typing import List
import collections
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers_start = []
        flowers_end = []
        res = []
        
        for start, end in flowers:
            flowers_start.append(start)
            flowers_end.append(end)

        flowers_start.sort()
        flowers_end.sort()
        cache = {}

        for day in people:
            if day in cache:
                res.append(cache[day])
                continue
                
            start = bisect.bisect_right(flowers_start, day)
            end = bisect.bisect_left(flowers_end, day)
            cache[day] = start - end
            res.append(cache[day])
        
        return res

    # memory limit exceeded
    # def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
    #     flowers_bloom = collections.Counter()

    #     for start, finish in flowers:
    #         for day in range(start, finish + 1):
    #             flowers_bloom[day] += 1
        
    #     return [flowers_bloom.get(day, 0) for day in people]
        
def main():
    sol = Solution()
    print(sol.fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
    print(sol.fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))

if __name__ == '__main__':
    main()