class Graph:
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


obj = Graph()
obj.add_node("A")
obj.add_node("B")
obj.add_node("C")
obj.add_node("D")
obj.add_node("E")
print(obj.graph)
obj.add_edge_weighted("A", "B", 5)
obj.add_edge_weighted("A", "C", 10)
obj.add_edge_weighted("A", "D", 12)
obj.add_edge_weighted("B", "D", 13)
obj.add_edge_weighted("B", "E", 8)
obj.add_edge_weighted("C", "D", 15)
obj.add_edge_weighted("D", "E", 15)
print(obj.graph)
# obj.delete_weighted_node("E")
# print(obj.graph)
obj.delete_weighted_edge("D", "A", 12)
print(obj.graph)
