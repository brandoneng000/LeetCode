from typing import List
import collections

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        graph = {}
        stack = [startGene]
        while stack:
            cur_gene = stack.pop()
            graph[cur_gene] = []
            for gene in bank:
                if self.check_gene_difference(cur_gene, gene) == 1:
                    graph[cur_gene].append(gene)
                    if gene not in graph:
                        stack.append(gene)
        
        def dfs(cur_gene: str, visited: set):
            if cur_gene == endGene:
                return 0
            
            min_mutation = float('inf')
            for gene in graph[cur_gene]:
                if gene not in visited:
                    visited.add(gene)
                    min_mutation = min(min_mutation, dfs(gene, visited))
                    visited.remove(gene)

            return min_mutation + 1

        mutations = dfs(startGene, set())
        return mutations if mutations != float('inf') else -1

    def check_gene_difference(self, cur_gene: str, mutation: str) -> int:
        return sum(cur_gene[i] != mutation[i] for i in range(len(cur_gene)))

def main():
    sol = Solution()
    print(sol.minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))
    print(sol.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
    print(sol.minMutation(startGene = "AAAACCCC", endGene = "CCCCCCCC", bank = 
        ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
    ))

if __name__ == '__main__':
    main()