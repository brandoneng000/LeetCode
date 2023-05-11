from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        cur_char = ""
        second_index = 0
        for index, c in enumerate(chars):
            if c == cur_char:
                count += 1
                if index == len(chars) - 1 and count > 1:
                    for digit in str(count):
                            chars[second_index] = digit
                            second_index += 1
            else:
                if count > 1:
                    for digit in str(count):
                        chars[second_index] = digit
                        second_index += 1
                cur_char = c
                chars[second_index] = cur_char
                second_index += 1
                count = 1
            
        return second_index

def main():
    sol = Solution()
    print(sol.compress(["a","a","b","b","c","c","c"]))
    print(sol.compress(["a"]))
    print(sol.compress(["a", "a"]))
    print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(sol.compress(["1","1","2"]))

if __name__ == '__main__':
    main()