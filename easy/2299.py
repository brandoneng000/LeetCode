import string

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # lower = upper = digit = symbol = False
        # prev = ""

        # for letter in password:
        #     if prev != letter:
        #         prev = letter
        #     else:
        #         return False

        #     if not lower and letter in string.ascii_lowercase:
        #         lower = True
        #         continue
            
        #     if not upper and letter in string.ascii_uppercase:
        #         upper = True
        #         continue
            
        #     if not digit and letter in string.digits:
        #         digit = True
        #         continue
            
        #     if not symbol and letter in "!@#$%^&*()-+":
        #         symbol = True
        #         continue

        # return lower and upper and digit and symbol and len(password) >= 8

        # res = len(password) >= 8
        # res = res and any(letter in password for letter in string.ascii_lowercase)
        # res = res and any(letter in password for letter in string.ascii_uppercase)
        # res = res and any(letter in password for letter in string.digits)
        # res = res and any(letter in password for letter in "!@#$%^&*()-+")
        # res = res and (not any(password[index] == password[index + 1] for index in range(len(password) - 1)))
        # return res
        
        prev = ""
        found = set()
        for letter in password:
            if prev != letter:
                prev = letter
            else:
                return False
            
            if letter.islower():
                found.add('l')
            elif letter.isupper():
                found.add('u')
            elif letter.isdigit():
                found.add('d')
            else:
                found.add('s')
            
        return len(password) >= 8 and len(found) == 4


def main():
    sol = Solution()
    print(sol.strongPasswordCheckerII("IloveLe3tcode!"))
    print(sol.strongPasswordCheckerII("Me+You--IsMyDream"))
    print(sol.strongPasswordCheckerII("1aB!"))
    print(sol.strongPasswordCheckerII("IloveLeeeeeee3tcode!"))
    print(sol.strongPasswordCheckerII("aA0!bB1@@3rbHkB8Puvl"))

if __name__ == '__main__':
    main()