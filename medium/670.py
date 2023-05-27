class Solution:
    def maximumSwap(self, num: int) -> int:
        # num_list = [int(n) for n in str(num)]
        num_list = list(str(num))
        num_last_index = {}
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] not in num_last_index:
                num_last_index[num_list[i]] = i

        keys = sorted(num_last_index.keys(), reverse=True)
        for i in range(len(num_list)):
            for j in keys:
                if num_list[i] < j and num_last_index[j] > i:
                    num_list[i], num_list[num_last_index[j]] = num_list[num_last_index[j]], num_list[i]
                    return int("".join(num_list))
        
        return num
        
        # num_list = list(str(num))

        # for i in range(len(num_list)):
        #     larger = i
        #     for j in range(len(num_list) - 1, i, -1):
        #         if num_list[j] > num_list[larger]:
        #             larger = j
        #     if larger != i:
        #         num_list[larger], num_list[i] = num_list[i], num_list[larger]
        #         break
        
        # return int("".join(num_list))


def main():
    sol = Solution()
    print(sol.maximumSwap(2736))
    print(sol.maximumSwap(9973))

if __name__ == '__main__':
    main()