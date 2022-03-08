from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_index = {}
        common_check = {}
        result = []

        for index, name in enumerate(list1):
            common_check[name] = False
            least_index[name] = index

        for index, name in enumerate(list2):
            if name in common_check:
                common_check[name] = True
                least_index[name] += index

        for name in common_check:
            if not common_check[name]:
                del least_index[name]

        least = min(least_index.values())
        for name in least_index:
            if least_index[name] == least:
                result.append(name)

        return result

def main():
    sol = Solution()
    print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
    print(sol.findRestaurant(["asdf","qwerty"], ["qwerty","asdf"]))

if __name__ == '__main__':
    main()