import sys
from typing import List
from queue import PriorityQueue

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.__graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def Dijkstra(self, src):
        # nodes_queue = PriorityQueue()
        nodes_set = self.__graph.get_all_v()
        dist = []
        prev = []
        dist[src] = 0
        for n in self.__graph.get_all_v():
            if n != src:
                dist[n.get_ID()] = sys.maxsize
                prev[n.get_ID()] = None
            # nodes_queue.put(n.get_ID, dist[n.get_ID])

        while nodes_set:
            u = self._get_min(dist, nodes_set)
            nodes_set.pop(u)
            for neighbor in u.get_neighbors_list():
                edges_of_u = self.__graph.all_out_edges_of_node(u.get_ID())
                if neighbor in nodes_set:
                    tmp_dist = dist[u.get_ID()] + edges_of_u[u][neighbor]
                    if tmp_dist < dist[neighbor.get_ID()]:
                        dist[neighbor.get_ID()] = tmp_dist
                        prev[neighbor.get_ID()] = u.get_ID()
        return dist, prev

    def _get_min(self, dist, node_set) -> NodeData:
        min_dist = sys.maxsize
        index_of_min_dist = 0
        for distence in dist:
            if distence < min_dist:
                min_dist = distence
                index_of_min_dist = dist.index(distence)
        return node_set.get(index_of_min_dist)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dijkstra_out = self.Dijkstra(id1)
        shortest_path_dist = dijkstra_out[0]
        shortest_path = List[int]
        for n in dijkstra_out[1]:
            shortest_path.append(n)
        return shortest_path_dist[id2], shortest_path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        minPath = sys.maxsize
        min_list = List[int]
        for node in node_lst:
            for n in node_lst:
                pass
        return None

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass


