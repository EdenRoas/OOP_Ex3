import json
import math
import sys
from typing import List
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from Point3D import Point3D
from queue import PriorityQueue
from GUI import GraphGUI

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.__graph = DiGraph()
        if graph is not None:
            for node in graph.get_all_v().values():
                self.__graph.add_node(node.get_ID(), (node.get_location().get_x(), node.get_location().get_y(),
                                                      node.get_location().get_z()))
            for src in graph.get_all_src_dict().keys():
                for dest in graph.all_out_edges_of_node(src).keys():
                    self.__graph.add_edge(src, dest, graph.get_edge_weigth(src, dest))

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as f:  # Open a file for reading
                Jsonfile = json.load(f)
            graph = DiGraph()
            for node in Jsonfile["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    graph.add_node(node['id'], pos)
                else:
                    graph.add_node(node['id'])

            for edge in Jsonfile["Edges"]:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.__graph = graph
            return True
        except Exception as e:
            print(e)
            return False

    # def load_from_json(self, file_name: str) -> bool:
    #     # try:
    #     #     with open(file_name, "r") as infile:
    #     #         graph_dict = json.load(infile)
    #     #         for node in graph_dict["Nodes"]:
    #     #             self.__graph.add_node(node.get_ID(), (node.get_location().x(), node.get_location().y(), node.get_location().z()))
    #     #         for edge in graph_dict["Edges"]:
    #     #             self.__graph.add_edge(edge["src"], edge["dest"], edge["w"])
    #     #     return True
    #     # return False
    #
    #     pass

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as f:  # Open a file for writing
                f.write(repr(self.__graph))
                return True
        except Exception as e:
            print(e)
            return False

    def Dijkstra(self, src) -> (list[int], list[int]):
        # nodes_set = self.__graph.get_all_v()
        dist = {src: 0}
        for node in self.__graph.get_all_v().keys():
            if node == src:
                continue
            dist[node] = math.inf
        parantMap = {}
        for node in self.__graph.get_all_v().keys():
            parantMap[node] = None
        heap_queue = PriorityQueue()
        # nq = NodeQueue(0, src)
        heap_queue.put((0, src))
        # print(heap_queue.__repr__())
        while not heap_queue.empty():
            v = heap_queue.get()
            # print(heap_queue.__repr__())
            if v[1] not in self.__graph.get_all_src_dict():
                break
            for neighbor in self.__graph.all_out_edges_of_node(v[1]).keys():
                old_dist = dist[neighbor]
                new_dist = dist[v[1]] + self.__graph.get_edge_weigth(v[1], neighbor)
                if new_dist < old_dist:
                    dist[neighbor] = new_dist
                    parantMap[neighbor] = v[1]
                    # nq = NodeQueue(new_dist, neighbor.get_ID())
                    heap_queue.put((new_dist, neighbor))
        return parantMap, dist

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.__graph.get_all_v() or id2 not in self.__graph.get_all_v():
            return math.inf, []
        if id1 is id2:
            return 0, [id1]
        parent, shortest_path_dist = self.Dijkstra(id1)
        if shortest_path_dist[id2] == math.inf:
            return math.inf, []
        path = []
        if id2 in parent:
            v = id2
            while v is not None:
                path.append(v)
                v = parent[v]
        return shortest_path_dist[id2], path[::-1]

    def centerPoint(self) -> (int, float):
        if not self.isConnected():
            return None, math.inf
        min_dist = sys.maxsize
        index_of_center = -1
        for node in self.__graph.get_all_v().keys():
            tmp_dist = self._find_max_dist(node)
            if tmp_dist < min_dist:
                min_dist = tmp_dist
                index_of_center = node
        return index_of_center, min_dist

    def _find_max_dist(self, cuur) -> float:
        max_dist = -sys.maxsize - 1
        for node in self.__graph.get_all_v().keys():
            shortest_path = self.shortest_path(cuur, node)[0]
            if shortest_path > max_dist:
                max_dist = shortest_path
        return max_dist

    def isConnected(self) -> bool:
        visited: {int: bool} = {}
        for node in self.__graph.get_all_v():
            visited[node] = None
        for node in self.__graph.get_all_v():
            self.DFS(node, visited)
        for b in visited:
            if not b:
                return False
        return True

    def DFS(self, cuur_node, visited):
        visited[cuur_node] = True
        for node in self.__graph.get_all_v()[cuur_node].get_neighbors_list():
            if not visited[node]:
                self.DFS(node, visited)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        sum_weight = 0
        path = []
        if len(node_lst) > 0:
            path.append(node_lst[0])
            src = node_lst[0]
            for node in node_lst[1:]:
                calculate = self.shortest_path(src, node)   #return the short path from the src in all the graph
                way = calculate[1]  #[list]
                sum_weight += calculate[0] #[weight]
                src = node
                for p in way[1:]:
                    path.append(p)
        if sum_weight == math.inf:
            return [], math.inf
        return path, sum_weight

    def plot_graph(self) -> None:
        graphdraw = GraphGUI(self)
        graphdraw.draw_graph()


