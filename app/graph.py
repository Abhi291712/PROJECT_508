class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths_util(self, u, d, visited, path, paths):
        visited[u] = True
        path.append(u)

        if u == d:
            paths.append(list(path))
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.print_all_paths_util(i, d, visited, path, paths)

        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d):
        visited = [False] * self.V
        path = []
        paths = []
        self.print_all_paths_util(s, d, visited, path, paths)
        return paths
