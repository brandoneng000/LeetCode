from heapq import heappop, heappush

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def get_next(input: int):
            input_arr = list(str(input))
            next_nums = []

            for i in range(len(input_arr)):
                if input_arr[i] != '9':
                    input_arr[i] = str(int(input_arr[i]) + 1)
                    next = int(''.join(input_arr))

                    if next not in primes:
                        next_nums.append(next)
                    input_arr[i] = str(int(input_arr[i]) - 1)

                if input_arr[i] != '0':
                    input_arr[i] = str(int(input_arr[i]) - 1)
                    next = int(''.join(input_arr))
                    
                    if next not in primes:
                        next_nums.append(next)

                    input_arr[i] = str(int(input_arr[i]) + 1)

            return next_nums

        INF = 10 ** 33
        max = 10 ** (len(str(n)))
        array = [x for x in range(2, max)]
        primes = set()

        for i, a in enumerate(array):
            if a != -1:
                primes.add(a)
                i = 1

                while a * i < max:
                    array[a * i - 2] = -1
                    i += 1

        if n in primes or m in primes:
            return -1

        if n == m:
            return n

        heap = [(n, n)]
        dists = [INF] * max

        while heap:
            cost, cur = heappop(heap)
            next_nums = get_next(cur)

            for next_node in next_nums:
                if next_node < 0:
                    continue

                next_cost = cost + next_node

                if next_node == m:
                    return next_cost

                if next_cost >= dists[next_node]:
                    continue

                heappush(heap, (next_cost, next_node))
                dists[next_node] = next_cost

        return -1

def main():
    sol = Solution()
    print(sol.minOperations(n = 10, m = 12))
    print(sol.minOperations(n = 4, m = 8))
    print(sol.minOperations(n = 6, m = 2))

if __name__ == '__main__':
    main()