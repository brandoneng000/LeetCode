from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_words = sentence.split()
        for root in dictionary:
            for i in range(len(sentence_words)):
                if sentence_words[i].startswith(root):
                    sentence_words[i] = root
        
        return " ".join(sentence_words)

def main():
    sol = Solution()
    print(sol.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
    print(sol.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))

if __name__ == '__main__':
    main()