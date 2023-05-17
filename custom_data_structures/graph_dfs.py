class BFS:
    def __init__(self):
        self.graph = {}
        self.visited_nodes = set()

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

    @staticmethod
    def dfs(node, visited_node, graph_dict):
        if node not in graph_dict:
            print(f"{node} node is not present in graph")
            return
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited_node:
                print(current, end=' ')
                visited_node.add(current)
                for node_value in graph_dict[current]:
                    stack.append(node_value)


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
obj.dfs("A", obj.visited_nodes, obj.graph)
