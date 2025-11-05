from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def clean():
            while hot and (hot[0][1] not in chosen or count[hot[0][1]] != hot[0][0]):
                heappop(hot)
            
            while pool and ((-pool[0][1]) in chosen or count[-pool[0][1]] != -pool[0][0] or -pool[0][0] == 0):
                heappop(pool)
        
        def demote_if_chosen(val: int):
            nonlocal total

            if val in chosen:
                chosen.remove(val)
                total -= val * count[val]
        
        def promote_if_needed():
            nonlocal total
            clean()
            while len(chosen) < x and pool:
                f, v = -pool[0][0], -pool[0][1]

                if count[v] != f or v in chosen or f == 0:
                    heappop(pool)
                    continue

                heappop(pool)
                chosen.add(v)
                total += v * f
                heappush(hot, (f, v))
            clean()

        def add_one(val: int):
            nonlocal total
            demote_if_chosen(val)
            f = count[val] + 1
            count[val] = f
            heappush(pool, (-f, -val))

            if len(chosen) < x:
                promote_if_needed()
            else:
                clean()
                
                if pool and hot:
                    bf, bv = -pool[0][0], -pool[0][1]
                    wf, wv = hot[0]

                    if bf > wf or (bf == wf and bv > wv):
                        heappop(pool)
                        chosen.add(bv)
                        total += bv * bf
                        heappush(hot, (bf, bv))

                        heappop(hot)

                        if wv in chosen:
                            chosen.remove(wv)
                            total -= wv * wf
                        heappush(pool, (-wf, -wv))
            clean()

        def remove_one(val: int):
            nonlocal total
            demote_if_chosen(val)
            f = count[val] - 1
            if f <= 0:
                count.pop(val)
            else:
                count[val] = f
                heappush(pool, (-f, -val))
            promote_if_needed()

        n = len(nums)
        res = []
        total = 0

        count = Counter()
        chosen = set()

        hot = []
        pool = []
        
        for i in range(k):
            add_one(nums[i])
        
        res.append(total)

        for i in range(k, n):
            remove_one(nums[i - k])
            add_one(nums[i])
            res.append(total)

        return res
        
def main():
    sol = Solution()
    print(sol.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
    print(sol.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2))

if __name__ == '__main__':
    main()