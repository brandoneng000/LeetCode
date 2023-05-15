def rand7():
    pass

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            index = (rand7() - 1) * 7 + rand7()
            if index <= 40:
                break
        
        return index % 10 + 1
        # res = 0

        # for _ in range(10):
        #     res += rand7()

        # return res % 10 + 1