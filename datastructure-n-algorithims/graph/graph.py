class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.items():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list.items():
            print(vertex[0], ":", vertex[1])


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.print_graph()
