class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Floyd–Warshall algorithm 
        # make a graph out of graph and equations (a,b) = val => a/b = val
        graph = {}

        for (u, v), val in zip(equations, values):
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = val
            graph[v][u] = 1 / val

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        res = []
        for u, v in queries:
            if u in graph and v in graph[u]:
                res.append(graph[u][v])
            else:
                res.append(-1.0)
        return res

        