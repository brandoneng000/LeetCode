from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        a = ord('a')

        for word in words:
            weight = 0

            for letter in word:
                weight += weights[ord(letter) - a]
            
            new_letter = 26 - (weight % 26) - 1
            res.append(chr(new_letter + a))
        
        return ''.join(res)
        

def main():
    sol = Solution()
    print(sol.mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
    print(sol.mapWordWeights(words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    print(sol.mapWordWeights(words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]))

if __name__ == '__main__':
    main()