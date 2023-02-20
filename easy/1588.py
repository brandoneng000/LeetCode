from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = sum(arr)

        for size in range(3, len(arr)):
            if size % 2:
                for index in range(len(arr) - size + 1):
                    result += sum(arr[index: index + size])
        
        result += sum(arr) if len(arr) % 2 and len(arr) > 2 else 0

        return result

def main():
    sol = Solution()
    print(sol.sumOddLengthSubarrays([1,4,2,5,3]))
    print(sol.sumOddLengthSubarrays([1,2]))
    print(sol.sumOddLengthSubarrays([10,11,12]))
    print(sol.sumOddLengthSubarrays([1,2,3,4,5,6]))


if __name__ == '__main__':
    main()