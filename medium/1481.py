from typing import List
import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n = len(arr)
        bucket = [[] for _ in range(n + 1)]
        arr_count = collections.Counter(arr)

        for val in arr_count:
            bucket[arr_count[val]].append(val)
        
        for count in range(n + 1):
            if k == 0:
                break
            while bucket[count] and k >= count:
                arr_count.pop(bucket[count].pop())
                k -= count
        
        return len(arr_count)


    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     arr_count = collections.Counter(arr)
    #     arr.sort(key=lambda x: (arr_count[x], x), reverse=True)

    #     return len(set(arr[:len(arr) - k]))

def main():
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts(arr = [24,119,157,446,251,117,22,168,374,373,323,311,441,213,120,412,200,236,328,24,164,104,331,32,19,223,89,114,152,82,456,381,355,343,157,245,443,368,229,49,82,16,373,142,240,125,8], k = 41))
    print(sol.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
    print(sol.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))

if __name__ == '__main__':
    main()