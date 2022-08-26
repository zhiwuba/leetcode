class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []

        def walk(node: int):
            if node == len(graph) -1:
                result.append(path.copy())
                return

            for i in graph[node]:
                path.append(i)
                walk(i)
                path.pop(-1)

        path = [0]
        walk(0)
        return result