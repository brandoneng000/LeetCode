import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        letter_count = collections.Counter(s)
        used = set()
        res = 0

        for letter, freq in letter_count.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        
        return res

    # def minDeletions(self, s: str) -> int:
    #     letter_freq = [0] * 26
    #     res = 0
        
    #     for letter in s:
    #         letter_freq[ord(letter) - ord('a')] += 1
        
    #     letter_freq.sort(reverse=True)

    #     for index in range(len(letter_freq)):
    #         while letter_freq.count(letter_freq[index]) > 1 and letter_freq[index] != 0:
    #             letter_freq[index] -= 1
    #             res += 1
        
    #     return res


    # def minDeletions(self, s: str) -> int:
    #     letter_count = collections.Counter(s)
    #     letter_freq = [[] for _ in range(s.count(max(s, key=s.count)) + 1)]

    #     for letter in letter_count:
    #         letter_freq[letter_count[letter]].append(letter)
        
    #     store = []
    #     res = 0

    #     for index in range(len(letter_freq) - 1, -1, -1):
    #         if not letter_freq[index] and store:
    #             res += store.pop() - index
    #         elif len(letter_freq[index]) > 1:
    #             store.extend([index] * (len(letter_freq[index]) - 1))
        
    #     return sum([res] + store)


def main():
    sol = Solution()
    print(sol.minDeletions("qwertyuiop"))
    print(sol.minDeletions("aab"))
    print(sol.minDeletions("aaabbbcc"))
    print(sol.minDeletions("ceabaacb"))

if __name__ == '__main__':
    main()