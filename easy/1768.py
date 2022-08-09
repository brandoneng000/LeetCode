class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        res = []
        
        while index < len(word1) and index < len(word2):
            res.append(word1[index])
            res.append(word2[index])
            index += 1
        
        return "".join(res) + word1[index:] + word2[index:]


def main():
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))
    print(sol.mergeAlternately("ab", "pqrs"))
    print(sol.mergeAlternately("abcd", "pq"))

if __name__ == '__main__':
    main()