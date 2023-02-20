from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # remove = len(arr) // 20

        # for _ in range(remove):
        #     arr.remove(min(arr))
        #     arr.remove(max(arr))
        
        # return sum(arr) / len(arr)

        # arr.sort()
        # remove = len(arr) // 20

        # for _ in range(remove):
        #     arr.pop(0)
        #     arr.pop()

        # return sum(arr) / len(arr)

        arr.sort()
        remove = len(arr) // 20

        return sum(arr[remove: len(arr) - remove]) / (len(arr) - remove * 2)


def main():
    sol = Solution()
    print(sol.trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
    print(sol.trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))
    print(sol.trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))

if __name__ == '__main__':
    main()