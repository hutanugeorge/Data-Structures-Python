class Graph:
    def __init__(self):
        self._number_of_nodes = 0
        self._adjacent_list = dict()

    def add_vertex(self, node):
        if node in self._adjacent_list:
            raise ValueError('You can\'t add 2 nodes wioth the same value!')
        self._adjacent_list[node] = []
        self._number_of_nodes += 1
        self._edge_list = dict()
        self._count_edges = 0
        return self

    def add_edge(self, node1, node2, directed = False, weighted = False):

        if (node1 or node2) not in self._adjacent_list:
            raise ValueError('This node isn\'t in  the graph!')
        elif node2 in self._adjacent_list[node1]:
            raise ValueError('This edge already exist!')
        elif node1 in self._adjacent_list[node2]:
            raise ValueError('This edge already exist!')

        if not directed:
            if not isinstance(weighted, int):
                self._adjacent_list[node1].append(node2)
                self._adjacent_list[node2].append(node1)
            else:
                self._adjacent_list[node1].append(node2)
                self._adjacent_list[node2].append(node1)
                self._edge_list[self._count_edges] = [node1, node2, weighted]
                self._count_edges += 1
        else:
            if not weighted:
                self._adjacent_list[node1].append(node2)
            else:
                self._adjacent_list[node1].append(node2)
                self._edge_list[self._count_edges] = [node1, node2, weighted]
                self._count_edges += 1

        return self

    def print(self):
        for i in self._adjacent_list:
            print(i, '-->', end = ' ')
            print([x for x in self._adjacent_list[i]])
        for j in self._edge_list:
            print(j, '-->', end = ' ')
            print([x for x in self._edge_list[j]])
