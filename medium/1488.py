from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        lakes = {}
        dry = []
        res = [-1] * n

        for i, r in enumerate(rains):
            if r == 0:
                dry.append(i)
            else:
                if r in lakes:
                    index = bisect.bisect(dry, lakes[r])
                    if index == len(dry):
                        return []
                    res[dry[index]] = r
                    dry.pop(index)
                lakes[r] = i

        for d in dry:
            res[d] = 1

        return res

        
def main():
    sol = Solution()
    print(sol.avoidFlood([0,1,1]))
    print(sol.avoidFlood([1,2,3,4]))
    print(sol.avoidFlood([1,2,0,0,2,1]))
    print(sol.avoidFlood([1,2,0,1,2]))

if __name__ == '__main__':
    main()