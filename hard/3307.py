from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        res = 0

        while k != 1:
            t = k.bit_length() - 1

            if (1 << t) == k:
                t -= 1
            
            k -= 1 << t

            if operations[t]:
                res += 1
        
        return chr((res % 26) + ord('a'))

    # def kthCharacter(self, k: int, operations: List[int]) -> str:
    #     word = ["a"]

    #     for op in operations:
    #         if op == 0:
    #             word.extend(word)
    #         else:
    #             temp = []

    #             for letter in word:
    #                 temp.append(chr((ord(letter) - ord('a') + 1) % 26 + ord('a')))

    #             word.extend(temp)
            
    #         if len(word) >= k:
    #             return word[k - 1]
        
        
        
def main():
    sol = Solution()
    print(sol.kthCharacter(k = 5, operations = [0,0,0]))
    print(sol.kthCharacter(k = 10, operations = [0,1,0,1]))

if __name__ == '__main__':
    main()