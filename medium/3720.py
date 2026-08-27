from typing import List

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def helper(freq: List[int], suffix: str):
            max_str = "".join(
                chr(i + a) * freq[i] for i in range(25, -1, -1) if freq[i] > 0
            )

            return max_str > suffix

        n = len(s)
        freq = [0] * 26
        a = ord('a')
        res = []

        for i in range(n):
            freq[ord(s[i]) - a] += 1

        for i in range(n):
            t = ord(target[i]) - a

            if freq[t] > 0:
                freq[t] -= 1

                if helper(freq, target[i + 1:]):
                    res.append(target[i])
                    continue

                freq[t] += 1

            for c in range(t + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    res.append(chr(c + a))
                    res.append(
                        "".join(chr(j + a) * freq[j] for j in range(26)) 
                    )
                    return ''.join(res)
            return ""
            
        return ""

        

def main():
    sol = Solution()
    print(sol.lexGreaterPermutation(s = "abc", target = "bba"))
    print(sol.lexGreaterPermutation(s = "leet", target = "code"))
    print(sol.lexGreaterPermutation(s = "baba", target = "bbaa"))

if __name__ == '__main__':
    main()