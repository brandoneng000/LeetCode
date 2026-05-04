from typing import List

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = ['']
        target = list(map(ord, target))
        a = ord('a')

        for num in target:
            letters = []

            for i in range(a, num + 1):
                letters.append(chr(i))
            
            prev = res[-1]
            for letter in letters:
                res.append(prev + letter)
        
        return res[1:]


        
def main():
    sol = Solution()
    print(sol.stringSequence("abc"))
    print(sol.stringSequence("he"))

if __name__ == '__main__':
    main()