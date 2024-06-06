from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []

        for word in queries:
            for dict_word in dictionary:
                cur = 0
                for i in range(n):
                    cur += word[i] != dict_word[i]
                
                if cur <= 2:
                    res.append(word)
                    break
        
        return res

        
def main():
    sol = Solution()
    print(sol.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]))
    print(sol.twoEditWords(queries = ["yes"], dictionary = ["not"]))

if __name__ == '__main__':
    main()