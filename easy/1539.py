from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        result = 0
        index = 0

        while index < len(arr):
            result += 1
            if result == arr[index]:
                index += 1
            else:
                k -= 1
                if k == 0:
                    break
        
        if k != 0:
            result += k

        return result
        


def main():
    sol = Solution()
    print(sol.findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(sol.findKthPositive(arr = [1,2,3,4], k = 2))

if __name__ == '__main__':
    main()