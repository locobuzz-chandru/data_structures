class BFS:
    def __init__(self):
        self.visited_nodes = []
        self.queue = []
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            print(node, " is already present in the graph")
        else:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            print(node1, "is not present in the graph")
        elif node2 not in self.graph:
            print(node2, "is not present in the graph")
        else:
            if node2 not in self.graph[node1]:
                self.graph[node1].append(node2)
                self.graph[node2].append(node1)

    def bfs(self, node, visited, graph_dict):
        visited.append(node)
        self.queue.append(node)
        while self.queue:
            m = self.queue.pop(0)
            print(m, end=" ")
            for node_value in graph_dict[m]:
                if node_value not in visited:
                    visited.append(node_value)
                    self.queue.append(node_value)


obj = BFS()
obj.add_node("A")
obj.add_node("B")
obj.add_node("C")
obj.add_node("D")
obj.add_node("E")
print(obj.graph)
obj.add_edge("A", "B")
obj.add_edge("B", "E")
obj.add_edge("A", "C")
obj.add_edge("A", "D")
obj.add_edge("B", "D")
obj.add_edge("C", "D")
obj.add_edge("E", "D")
print(obj.graph)
obj.bfs("A", obj.visited_nodes, obj.graph)
