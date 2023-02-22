from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for encode in encoded:
            arr.append(arr[-1] ^ encode)
        
        return arr

def main():
    sol = Solution()
    print(sol.decode(encoded = [1,2,3], first = 1))
    print(sol.decode(encoded = [6,2,7,3], first = 4))

if __name__ == '__main__':
    main()