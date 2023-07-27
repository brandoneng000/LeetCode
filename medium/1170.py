from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq_count(word: str):
            cur_letter = 'z'
            count = 0
            for letter in word:
                if letter < cur_letter:
                    cur_letter = letter
                    count = 1
                elif letter == cur_letter:
                    count += 1
            
            return count
        
        frequency = [0] * (len(max(words, key=len)) + 1)
        res = []

        for word in words:
            frequency[freq_count(word)] += 1
        
        for query in queries:
            res.append(sum(frequency[freq_count(query) + 1:]))
        
        return res

def main():
    sol = Solution()
    print(sol.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
    print(sol.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))

if __name__ == '__main__':
    main()