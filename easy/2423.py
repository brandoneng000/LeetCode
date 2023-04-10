import collections

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for index in range(len(word)):
            # print(word[:index] + word[index + 1:])
            letters_dict = collections.Counter(word[:index] + word[index + 1:])
            count_dict = collections.Counter(letters_dict.values())
            if len(count_dict) == 1:
                return True
            
        return False

def main():
    sol = Solution()
    print(sol.equalFrequency("abcc"))
    print(sol.equalFrequency("aazz"))
    print(sol.equalFrequency("aaaazz"))
    print(sol.equalFrequency("aca"))

if __name__ == '__main__':
    main()