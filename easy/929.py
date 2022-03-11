from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for email in emails:
            email = email.split("@")
            email[0] = email[0].replace(".", "")
            email[0] = email[0].split("+")[0]
            result.add("@".join(email))

        return len(result)
        
def main():
    sol = Solution()
    print(sol.numUniqueEmails([
        "test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"
    ]))
    print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))

if __name__ == '__main__':
    main()