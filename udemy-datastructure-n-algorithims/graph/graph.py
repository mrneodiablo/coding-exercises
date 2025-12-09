class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v2].remove(v1)
                self.adj_list[v1].remove(v2)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex) -> bool:
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                if vertex in self.adj_list[other_vertex]:
                    self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list.items():
            print(vertex[0], ":", vertex[1])


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")

    graph.add_edge("D", "B")
    graph.add_edge("D", "A")
    graph.add_edge("D", "C")

    graph.print_graph()
    print("+++++++++++++++++")
    graph.remove_vertex("D")
    graph.print_graph()
