from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for i in range(n, 0, -1):
            index = arr.index(i)
            if index == i - 1:
                continue
            if index != 0:
                res.append(index + 1)
                arr[:index + 1] = arr[:index + 1][::-1]
            res.append(i)
            arr[:i] = arr[:i][::-1]
        
        return res
        

def main():
    sol = Solution()
    print(sol.pancakeSort([3,2,4,1]))
    print(sol.pancakeSort([1,2,3]))

if __name__ == '__main__':
    main()