from typing import List
import collections

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                wins = 0
            wins += 1

            if wins == k:
                break
            
        return cur
        

    # def getWinner(self, arr: List[int], k: int) -> int:
    #     n = len(arr)
    #     if n <= k:
    #         return max(arr)

    #     cur = 0
    #     wins = 0
    #     arr_indexes = collections.deque(range(1, n))

    #     while wins < k:
    #         if arr[cur] > arr[arr_indexes[0]]:
    #             wins += 1
    #             arr_indexes.append(arr_indexes.popleft())
    #         else:
    #             wins = 1
    #             arr_indexes.append(cur)
    #             cur = arr_indexes.popleft()
        
    #     return arr[cur]


        
def main():
    sol = Solution()
    print(sol.getWinner(arr = [2,1,3,5,4,6,7], k = 2))
    print(sol.getWinner(arr = [3,2,1], k = 10))


if __name__ == '__main__':
    main()