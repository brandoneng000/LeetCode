from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        k_ticket_buyer = tickets[k]
        time = 0

        for index, val in enumerate(tickets):
            if index <= k:
                time += min(val, k_ticket_buyer)
            else:
                time += min(val, k_ticket_buyer - 1)
        
        return time


def main():
    sol = Solution()
    print(sol.timeRequiredToBuy(tickets = [2,3,2], k = 2))
    print(sol.timeRequiredToBuy(tickets = [5,1,1,1], k = 0))

if __name__ == '__main__':
    main()