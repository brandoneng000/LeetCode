from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr_count = defaultdict(list)
        res = [0] * n

        for i in range(n):
            arr_count[arr[i]].append(i)
        
        for key in arr_count:
            indexes = arr_count[key]
            prefix = [0] * (len(indexes) + 1)

            for i in range(len(indexes)):
                prefix[i + 1] = prefix[i] + indexes[i]
            
            for i, val in enumerate(indexes):
                res[val] = (val * (i + 1) - prefix[i + 1]) + ((prefix[len(indexes)] - prefix[i]) - val * (len(indexes) - i))
        
        return res
        
def main():
    sol = Solution()
    print(sol.getDistances([2,1,3,1,2,3,3]))
    print(sol.getDistances([10,5,10,10]))

if __name__ == '__main__':
    main()