from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        carry = 0
        while arr1 or arr2 or carry:
            val1 = val2 = 0
            if arr1:
                val1 = arr1.pop()
            
            if arr2:
                val2 = arr2.pop()
            
            carry += val1 + val2
            res.append(carry & 1)
            carry = -(carry >> 1)
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return res[::-1]

def main():
    sol = Solution()
    print(sol.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))
    print(sol.addNegabinary(arr1 = [0], arr2 = [0]))
    print(sol.addNegabinary(arr1 = [0], arr2 = [1]))

if __name__ == '__main__':
    main()