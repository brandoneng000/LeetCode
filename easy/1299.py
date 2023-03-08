from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = -1

        for index in range(1, len(arr) + 1):
            temp, arr[-index] = max(temp, arr[-index]), temp
        
        return arr

def main():
    sol = Solution()
    print(sol.replaceElements([17,18,5,4,6,1]))
    print(sol.replaceElements([400]))

if __name__ == '__main__':
    main()