from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        dif_candy_per_person = (sum(aliceSizes) - sum(bobSizes)) // 2
        
        aliceSizes = set(aliceSizes)
        for candy in set(bobSizes):
            if dif_candy_per_person + candy in aliceSizes:
                return [dif_candy_per_person + candy, candy]
            
        

def main():
    sol = Solution()
    print(sol.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))
    print(sol.fairCandySwap(aliceSizes = [1,2], bobSizes = [2,3]))
    print(sol.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))

if __name__ == '__main__':
    main()