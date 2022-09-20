class Solution:
    def replaceDigits(self, s: str) -> str:
        # solution using Regex
        # import re
        # res = []
        # numbers = re.findall('\d+', s)
        # letters = re.findall('[a-z]', s)

        # for index in range(len(numbers)):
        #     letter = letters[index]
        #     res.append(letter)
            
        #     shift = min(ord(letter) + int(numbers[index]), ord('z'))
        #     res.append(chr(shift))
        
        # if len(numbers) < len(letters):
        #     res.append(letters[-1])

        # return "".join(res)

        # solution 2
        # res = []

        # for index in range(len(s)):
        #     if index % 2 == 0:
        #         res.append(s[index])
        #     else:
        #         res.append(chr(ord(res[-1]) + int(s[index])))
        
        # return "".join(res)

        # solution 3
        res = []
        alt = True

        for letter in s:
            if alt: 
                res.append(letter)
            else:
                res.append(chr(ord(res[-1]) + int(letter)))
            alt = not alt
            
        return "".join(res)

def main():
    sol = Solution()
    print(sol.replaceDigits("a1c1e1"))
    print(sol.replaceDigits("a1b2c3d4e"))

if __name__ == '__main__':
    main()