import json
import sys
from typing import List
from HeapQueue import HeapQueue
from NodeQueue import NodeQueue
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.__graph = graph

    def GraphAlgo(self):
        graph = DiGraph()
        self.__init__(graph)

    def get_graph(self) -> GraphInterface:
        return self.__graph

    # def load_from_json(self, file_name: str) -> bool:
    #     try:
    #         with open(file_name, "r") as infile:
    #             graph_dict = json.load(infile)
    #             for node in graph_dict["Nodes"]:
    #                 self.__graph.add_node(node.get_ID(), (node.get_location().x(), node.get_location().y(), node.get_location().z()))
    #             for edge in graph_dict["Edges"]:
    #                 self.__graph.add_edge(edge["src"], edge["dest"], edge["w"])
    #         return True
    #     return False
    #
    #     pass
    #
    # def save_to_json(self, file_name: str) -> bool:
    #     json_object = json.dumps(dictionary, indent=4)
    #     with open(file_name, "w") as outfile:
    #         outfile.write(json_object)

    def Dijkstra(self, src, dest) -> (list[int], list[int]):
        # nodes_queue = PriorityQueue()
        global current_node
        nodes_set = self.__graph.get_all_v()
        dist = {src: 0}
        for node in nodes_set.keys():
            if node == src:
                continue
            dist[node] = sys.maxsize
        parantMap = {}
        for node in nodes_set.keys():
            dist[node] = None
        isVisit = []
        nq = NodeQueue(0, src)
        dist_heap = HeapQueue()
        dist_heap.push(nq)
        while dist_heap:
            while not dist_heap.is_empty():
                current_node = dist_heap.get_minimum()
                if current_node in isVisit:
                    break
            if dist_heap.is_empty():
                break
            isVisit.append(current_node)
            if current_node == dest:
                break
            for neighbor in nodes_set[current_node].get_neighbors_list():
                if neighbor in isVisit:
                    continue
                edges_of_current_node = self.__graph.all_out_edges_of_node(current_node)
                old_dist = dist.get(neighbor)
                new_dist = dist.get(current_node) + edges_of_current_node[current_node][neighbor]
                if new_dist < old_dist:
                    nq = NodeQueue(new_dist, neighbor)
                    dist_heap.push(nq)
                    dist[neighbor] = new_dist
                    parantMap[neighbor]  = current_node
        return parantMap, dist
        # for n in self.__graph.get_all_v():
        #     if n != src:
        #         dist[n.get_ID()] = sys.maxsize
        #         prev[n.get_ID()] = None
        #     # nodes_queue.put(n.get_ID, dist[n.get_ID])
        #
        # while nodes_set:
        #     u = self._get_min(dist, nodes_set)
        #     nodes_set.pop(u)
        #     for neighbor in u.get_neighbors_list():
        #         edges_of_u = self.__graph.all_out_edges_of_node(u.get_ID())
        #         if neighbor in nodes_set:
        #             tmp_dist = dist[u.get_ID()] + edges_of_u[u][neighbor]
        #             if tmp_dist < dist[neighbor.get_ID()]:
        #                 dist[neighbor.get_ID()] = tmp_dist
        #                 prev[neighbor.get_ID()] = u.get_ID()
        # return dist, prev

    # def _get_min(self, dist, node_set) -> NodeData:
    #     min_dist = sys.maxsize
    #     index_of_min_dist = 0
    #     for distence in dist:
    #         if distence < min_dist:
    #             min_dist = distence
    #             index_of_min_dist = dist.index(distence)
    #     return node_set.get(index_of_min_dist)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dijkstra_out = self.Dijkstra(id1, id2)
        shortest_path_dist = dijkstra_out[1]
        path = []
        parent = dijkstra_out[0]
        if id2 in parent:
            v = id2
            while v is not None:
                path.append(v)
                v = parent[v]
        return shortest_path_dist[id2], path[::-1]

    def centerPoint(self) -> (int, float):
        id_of_center = 0
        min_max_dist = sys.maxsize
        for node in self.__graph.get_all_v():
            dist = self.Dijkstra(node)[0]
            # min_max_dist = self._find_max_dist(dist)
            if dist.max() < min_max_dist:
                min_max_dist = dist.max()
                id_of_center = node
        return id_of_center, min_max_dist

    # def _find_max_dist(self, dist):
    #     max_dist =
    #     for d in dist:
    #
    #     pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        minPath = sys.maxsize
        min_list = List[int]
        for node in node_lst:
            for n in node_lst:
                pass
        return None

    def plot_graph(self) -> None:
        pass


