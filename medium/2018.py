from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def check_match(word: str, check: str):
            for w, c in zip(word, check):
                if w != c and c != ' ':
                    return False
            
            return True

        m, n = len(board), len(board[0])
        rev_word = word[::-1]
        word_len = len(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] != '#':
                    cur = []
                    index = i
                    if i == 0:
                        while index < m and board[index][j] != '#' and len(cur) <= word_len:
                            cur.append(board[index][j])
                            index += 1
                    elif i > 0 and board[i - 1][j] == '#':
                        while index < m and board[index][j] != '#' and len(cur) <= word_len:
                            cur.append(board[index][j])
                            index += 1
                    check = "".join(cur)
                    if len(check) == word_len and (check_match(word, check) or check_match(rev_word, check)):
                        return True
                    
                    cur = []
                    index = j
                    if j == 0:
                        while index < n and board[i][index] != '#' and len(cur) <= word_len:
                            cur.append(board[i][index])
                            index += 1
                    elif j > 0 and board[i][j - 1] == '#':
                        while index < n and board[i][index] != '#' and len(cur) <= word_len:
                            cur.append(board[i][index])
                            index += 1

                    check = "".join(cur)
                    if len(check) == word_len and (check_match(word, check) or check_match(rev_word, check)):
                        return True

        
        return False
        
def main():
    sol = Solution()
    print(sol.placeWordInCrossword(board = [[" "],["#"],["o"],[" "],["t"],["m"],["o"],[" "],["#"],[" "]], word = "octmor"))
    print(sol.placeWordInCrossword(board = [[" "," "],[" "," "]], word = "a"))
    print(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"))
    print(sol.placeWordInCrossword(board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"))
    print(sol.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"))

if __name__ == '__main__':
    main()