from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        start, end = 0, 0
        longest = 0

        while start < len(arr):
            end = start
            if end < len(arr) - 1 and arr[end] < arr[end + 1]:
                while end < len(arr) - 1 and arr[end] < arr[end + 1]:
                    end += 1
                if end < len(arr) - 1 and arr[end] > arr[end + 1]:
                    while end < len(arr) - 1 and arr[end] > arr[end + 1]:
                        end += 1
                    longest = max(longest, end - start + 1)

            start = max(end, start + 1)
        
        return longest
            

def main():
    sol = Solution()
    print(sol.longestMountain([2,1,4,7,3,2,5]))
    print(sol.longestMountain([2,2,2]))

if __name__ == '__main__':
    main()