from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: bin(x).count('1'))
        return arr

def main():
    sol = Solution()
    print(sol.sortByBits([0,1,2,3,4,5,6,7,8]))
    print(sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))

if __name__ == '__main__':
    main()