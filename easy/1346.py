from typing import List
from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter(arr)

        if count[0] >= 2:
            return True
        
        for num in count:
            if num != 0 and num * 2 in count:
                return True
        
        return False

    # def checkIfExist(self, arr: List[int]) -> bool:
    #     if arr.count(0) >= 2:
    #         return True

    #     divide = [num // 2 for num in arr if num % 2 == 0 and num != 0]
        
    #     for num in divide:
    #         if num in arr:
    #             return True
    #     return False

def main():
    sol = Solution()
    print(sol.checkIfExist([10,2,5,3]))
    print(sol.checkIfExist([3,1,7,11]))

if __name__ == '__main__':
    main()