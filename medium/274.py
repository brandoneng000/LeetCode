from typing import List
import heapq

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse=True)
        # for i in range(len(citations)):
        #     if i + 1 > citations[i]:
        #         return i
        
        # return len(citations)
        cit = [-c for c in citations.copy()]
        heapq.heapify(cit)
        for i in range(len(cit)):
            if i + 1 > -heapq.heappop(cit):
                return i
            
        return len(citations)

def main():
    sol = Solution()
    print(sol.hIndex([3,0,6,1,5]))
    print(sol.hIndex([1,3,1]))

if __name__ == '__main__':
    main()