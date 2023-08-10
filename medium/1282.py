from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        res = []

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        
        for size in groups:
            res.extend(groups[size][i: i + size] for i in range(0, len(groups[size]), size))
        
        return res


def main():
    sol = Solution()
    print(sol.groupThePeople([3,3,3,3,3,1,3]))
    print(sol.groupThePeople([2,1,3,3,3,2]))

if __name__ == '__main__':
    main()