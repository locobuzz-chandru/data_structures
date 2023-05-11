class ClassGraph:
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.node_count = 0

    def add_node(self, node):
        if node in self.nodes:
            return f'{node} is already present in the graph'
        self.node_count = self.node_count + 1
        self.nodes.append(node)
        for row_list in self.graph:
            row_list.append(0)
        temp = []
        for columns in range(self.node_count):
            temp.append(0)
        self.graph.append(temp)

    def add_edge_weighted(self, node1, node2, cost):
        if node1 not in self.nodes:
            return f'{node1} is not present in the graph'
        elif node2 not in self.nodes:
            return f'{node2} is not present in the graph'
        else:
            index1 = self.nodes.index(node1)
            index2 = self.nodes.index(node2)
            self.graph[index1][index2] = cost
            self.graph[index2][index1] = cost

    def delete_node(self, node):
        if node not in self.nodes:
            return f'{node} is not present in the graph'
        else:
            index1 = self.nodes.index(node)
            self.node_count = self.node_count - 1
            self.nodes.remove(node)
            self.graph.pop(index1)  # deletes row
            for row_list in self.graph:
                row_list.pop(index1)

    def delete_edge(self, node1, node2):
        if node1 not in self.nodes:
            return f'{node1} is not present in the graph'
        elif node2 not in self.nodes:
            return f'{node2} is not present in the graph'
        else:
            index1 = self.nodes.index(node1)
            index2 = self.nodes.index(node2)
            self.graph[index1][index2] = 0
            self.graph[index2][index1] = 0

    def print_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(format(self.graph[i][j], "<5"), end=' ')
            print()


obj = ClassGraph()
obj.add_node("A")
obj.add_node("B")
obj.add_node("C")
obj.add_node("D")
print(obj.nodes)
# print(graph)
obj.add_edge_weighted("A", "C", 10)
obj.add_edge_weighted("D", "C", 8)
obj.add_edge_weighted("A", "B", 5)
obj.add_edge_weighted("A", "D", 12)
obj.add_edge_weighted("B", "C", 15)
obj.print_graph()
# print()
# obj.delete_node("B")
# obj.print_graph()
