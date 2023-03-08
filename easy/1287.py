from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # arr_count = {}

        # for num in arr:
        #     arr_count[num] = arr_count.get(num, 0) + 1
        
        # return max(arr_count, key=lambda x: arr_count[x])
        size, gap = len(arr), len(arr) // 4
        for index in range(size - gap):
            if arr[index] == arr[index + gap]:
                return arr[index]
        
        return -1

def main():
    sol = Solution()
    print(sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]))
    print(sol.findSpecialInteger([1,1]))

if __name__ == '__main__':
    main()