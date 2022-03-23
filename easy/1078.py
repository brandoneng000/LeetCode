from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        sentence = text.split()
        third = []

        for index in range(2, len(sentence)):
            if sentence[index - 2] == first and sentence[index - 1] == second:
                third.append(sentence[index])

        return third

        
def main():
    sol = Solution()
    print(sol.findOcurrences("alice is a good girl she is a good student", "a", "good"))

if __name__ == '__main__':
    main()