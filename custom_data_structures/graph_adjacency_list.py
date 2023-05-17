class ClassGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            return f'{node} is already present in the graph'
        self.graph[node] = []

    def add_edge_weighted(self, node1, node2, cost):
        if node1 not in self.graph:
            return f'{node1} is not present in the graph'
        elif node2 not in self.graph:
            return f'{node2} is not present in the graph'
        else:
            self.graph[node1].append([node2, cost])
            self.graph[node2].append([node1, cost])

    def delete_weighted_node(self, node):
        if node not in self.graph:
            return f'{node} is not present in the graph'
        else:
            self.graph.pop(node)
            for key in self.graph:
                values_list = self.graph[key]
                for weighted_values_list in values_list:
                    if node == weighted_values_list[0]:
                        values_list.remove(weighted_values_list)
                        break

    def delete_weighted_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            return f'{node1} is not present in the graph'
        elif node2 not in self.graph:
            return f'{node2} is not present in the graph'
        else:
            if [node2, cost] in self.graph[node1]:
                self.graph[node1].remove([node2, cost])
                self.graph[node2].remove([node1, cost])


obj = ClassGraph()
obj.add_node("A")
obj.add_node("B")
obj.add_node("C")
obj.add_node("D")
print(obj.graph)
obj.add_edge_weighted("A", "D", 10)
obj.add_edge_weighted("C", "B", 8)
obj.add_edge_weighted("A", "B", 6)
print(obj.graph)
# obj.delete_weighted_node("C")
# print(obj.graph)
# obj.delete_weighted_edge("D", "A", 10)
# print(obj.graph)

