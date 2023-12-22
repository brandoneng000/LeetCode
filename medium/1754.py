class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = []
        index1 = index2 = 0

        while index1 < m and index2 < n:
            if word1[index1] > word2[index2]:
                res.append(word1[index1])
                index1 += 1
            elif word1[index1] < word2[index2]:
                res.append(word2[index2])
                index2 += 1
            else:
                temp1, temp2 = word1[index1:], word2[index2:]
                if temp1 >= temp2:
                    res.append(word1[index1])
                    index1 += 1
                elif temp1 < temp2:
                    res.append(word2[index2])
                    index2 += 1
        
        res.append(word1[index1:])
        res.append(word2[index2:])

        return "".join(res)

        
def main():
    sol = Solution()
    print(sol.largestMerge(word1 = "cabaa", word2 = "bcaaa"))
    print(sol.largestMerge(word1 = "abcabc", word2 = "abdcaba"))

if __name__ == '__main__':
    main()