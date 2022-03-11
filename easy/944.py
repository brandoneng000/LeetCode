from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        for col in zip(*strs):
            for index in range(len(strs) - 1):
                if col[index] > col[index + 1]:
                    result += 1
                    break

        return result
        
        # columns = [*range(len(strs[0]))]
        # letters = dict.fromkeys(range(len(strs[0])))
        # for letter in letters:
        #     letters[letter] = -1
        
        # for word in strs:
        #     for col in columns:
        #         if letters[col] <= ord(word[col]):
        #             letters[col] = ord(word[col])
        #         else:
        #             columns.remove(col)
        
        # return len(strs[0]) - len(columns)

        # delete = 0
        
        # columns = dict.fromkeys(range(len(strs[0])))
        # for col in columns:
        #     columns[col] = -1

        # for word in strs:
        #     for index, letter in enumerate(word):
        #         if columns[index] <= ord(letter):
        #             columns[index] = ord(letter)
        #         elif columns[index] == 100000:
        #             pass
        #         else:
        #             delete += 1
        #             columns[index] = 100000

        # return delete

def main():
    sol = Solution()
    print(sol.minDeletionSize([
        "cba","daf","ghi"
    ]))
    print(sol.minDeletionSize([
        "a","b"
    ]))
    print(sol.minDeletionSize([
        "zyx","wvu","tsr"
    ]))
    print(sol.minDeletionSize([
        "rrjk","furt","guzm"
    ]))

if __name__ == '__main__':
    main()