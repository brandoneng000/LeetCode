from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        def check_letters(letters: set[str], keyboard: str) -> bool:
            for letter in letters:
                if letter not in keyboard:
                    return False
            
            return True

        result = []
        keyboard = { 0:"qwertyuiop", 1:"asdfghjkl", 2:"zxcvbnm"}
        
        keyboard[0] += keyboard[0].upper()
        keyboard[1] += keyboard[1].upper()
        keyboard[2] += keyboard[2].upper()
        
        for word in words:
            letters = set(word)
            for num in range(3):
                if check_letters(letters, keyboard[num]):
                    result.append(word)
                    break
                        
        return result
            
        
def main():
    sol = Solution()
    print(sol.findWords(["Hello","Alaska","Dad","Peace"]))

if __name__ == '__main__':
    main()