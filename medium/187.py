from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        dna = set()

        for i in range(len(s) - 10 + 1):
            if s[i: i + 10] in dna:
                res.add(s[i: i + 10])
            else:
                dna.add(s[i: i + 10])

        return list(res)

def main():
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    print(sol.findRepeatedDnaSequences("AAAAAAAAAAA"))

if __name__ == '__main__':
    main()