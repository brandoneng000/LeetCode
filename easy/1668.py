class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        repeat_word = word

        while len(repeat_word) <= len(sequence):
            if repeat_word in sequence:
                repeat_word += word
            else:
                break

        return (len(repeat_word) // len(word)) - 1

        
def main():
    sol = Solution()
    print(sol.maxRepeating("ababc", "ab"))
    print(sol.maxRepeating("ababc", "ba"))
    print(sol.maxRepeating("ababc", "ac"))
    print(sol.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
    # "aaaba aaab aaaba aaaba aaaba aaaba aaaba"

if __name__ == '__main__':
    main()