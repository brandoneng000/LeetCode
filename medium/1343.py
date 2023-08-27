from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        avg_arr = [a / k for a  in arr]
        cur = sum(avg_arr[:k])
        res += cur >= threshold

        for i in range(k, len(avg_arr)):
            cur -= avg_arr[i - k]
            cur += avg_arr[i]

            res += cur >= threshold

        return res

def main():
    sol = Solution()
    print(sol.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
    print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))

if __name__ == '__main__':
    main()