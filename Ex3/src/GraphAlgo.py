import json
import math
import sys
from typing import List
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData
from queue import PriorityQueue


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
        # try:
        #     with open(file_name, "r") as infile:
        #         graph_dict = json.load(infile)
        #         for node in graph_dict["Nodes"]:
        #             self.__graph.add_node(node.get_ID(), (node.get_location().x(), node.get_location().y(), node.get_location().z()))
        #         for edge in graph_dict["Edges"]:
        #             self.__graph.add_edge(edge["src"], edge["dest"], edge["w"])
        #     return True
        # return False

        pass

    def save_to_json(self, file_name: str) -> bool:
        # json_object = json.dumps(dictionary, indent=4)
        # with open(file_name, "w") as outfile:
        #     outfile.write(json_object)
        pass

    # def Dijkstra(self, src, dest) -> (list[int], list[int]):
    #     global current_node
    #     nodes_set = self.__graph.get_all_v()
    #     dist = {src: 0}
    #     for node in nodes_set.keys():
    #         if node == src:
    #             continue
    #         dist[node] = math.inf
    #     parantMap = {}
    #     for node in nodes_set.keys():
    #         parantMap[node] = None
    #     isVisit = []
    #     nq = NodeQueue(0, src)
    #     dist_heap = HeapQueue()
    #     dist_heap.push(nq)
    #     # while dist_heap:
    #     while not dist_heap.is_empty():
    #         current_node = dist_heap.get_minimum()
    #         if current_node in isVisit:
    #             # break
    #             continue
    #         # if dist_heap.is_empty():
    #         #     break
    #         isVisit.append(current_node)
    #         # if current_node == dest:
    #         #     break
    #         for neighbor in nodes_set[current_node].get_neighbors_list():
    #             if neighbor in isVisit:
    #                 continue
    #             edges_of_current_node = self.__graph.all_out_edges_of_node(current_node)
    #             old_dist = dist.get(neighbor)
    #             new_dist = dist.get(current_node) + edges_of_current_node[current_node][neighbor]
    #             if new_dist < old_dist:
    #                 nq = NodeQueue(new_dist, neighbor)
    #                 dist_heap.push(nq)
    #                 dist[neighbor] = new_dist
    #                 parantMap[neighbor]  = current_node
    #     return parantMap, dist
    #     # for n in self.__graph.get_all_v():
    #     #     if n != src:
    #     #         dist[n.get_ID()] = sys.maxsize
    #     #         prev[n.get_ID()] = None
    #     #     # nodes_queue.put(n.get_ID, dist[n.get_ID])
    #     #
    #     # while nodes_set:
    #     #     u = self._get_min(dist, nodes_set)
    #     #     nodes_set.pop(u)
    #     #     for neighbor in u.get_neighbors_list():
    #     #         edges_of_u = self.__graph.all_out_edges_of_node(u.get_ID())
    #     #         if neighbor in nodes_set:
    #     #             tmp_dist = dist[u.get_ID()] + edges_of_u[u][neighbor]
    #     #             if tmp_dist < dist[neighbor.get_ID()]:
    #     #                 dist[neighbor.get_ID()] = tmp_dist
    #     #                 prev[neighbor.get_ID()] = u.get_ID()
    #     # return dist, prev
    #
    # # def _get_min(self, dist, node_set) -> NodeData:
    # #     min_dist = sys.maxsize
    # #     index_of_min_dist = 0
    # #     for distence in dist:
    # #         if distence < min_dist:
    # #             min_dist = distence
    # #             index_of_min_dist = dist.index(distence)
    # #     return node_set.get(index_of_min_dist)

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
        path = []
        if id2 in parent:
            v = id2
            while v is not None:
                path.append(v)
                v = parent[v]
        return shortest_path_dist[id2], path[::-1]

    def centerPoint(self) -> (int, float):
        id_of_center = 0
        all_v_dict: {int: list} = {}
        minimus_distances: {int: float} = {}
        for node_src in self.__graph.get_all_v():
            for node_dest in self.__graph.get_all_v():
                tmp_dist = self.shortest_path(node_src, node_dest)
                all_v_dict[node_src] = []
                all_v_dict[node_src].append(tmp_dist)
        for arr in all_v_dict.keys():
            min_dist = self._find_min_dist(all_v_dict[arr])
            minimus_distances[arr] = min_dist
        min_max_dist = minimus_distances[0]
        for dist in minimus_distances:
            if dist > min_max_dist[0]:
                min_max_dist = dist
        return id_of_center, min_max_dist

        # for node in self.__graph.get_all_v():
        #     dist = self.Dijkstra(node)[1]
        #     min_max_dist = self._find_max_dist(dist)
        #     if min_max_dist < min_max_dist:
        #         min_max_dist = min_max_dist
        #         id_of_center = node
        # return id_of_center, min_max_dist
    def _find_min_dist(self, array: list):
        min_dist = sys.maxsize
        for d in array:
            if d[0] < min_dist:
                min_dist = d
        return min_dist

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
        return path, sum_weight

    def plot_graph(self) -> None:
        pass


