from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            return f'{node} is already present in the graph'
        self.graph[node] = []

    def add_edge_unweighted(self, node1, node2):
        if node1 not in self.graph:
            return f'{node1} is not present in the graph'
        elif node2 not in self.graph:
            return f'{node2} is not present in the graph'
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        print(start, end=' ')
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


if __name__ == '__main__':
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    # print(g.graph)
    g.add_edge_unweighted("A", "B")
    g.add_edge_unweighted("A", "C")
    g.add_edge_unweighted("B", "D")
    g.add_edge_unweighted("C", "D")
    print(g.graph)
    g.bfs('A')
    print()
    g.dfs('A')
    print()
