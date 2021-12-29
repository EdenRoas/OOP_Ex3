import json
import math
import sys
import time
from typing import List

from pip._internal.cli.cmdoptions import src

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
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
        # begin = time.time()
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
            # end = time.time()
            # print("the time it took for the function load_from_json to run is: {} sec.".format(end - begin))
            return True
        except Exception as e:
            print(e)
            # end = time.time()
            # print("the time it took for the function load_from_json to run is: {} sec.".format(end - begin))
            return False

    def save_to_json(self, file_name: str) -> bool:
        # begin = time.time()
        dictionary = {}
        dictionary["Edges"] = []
        for src in self.__graph.get_all_src_dict().keys():
            for dest in self.__graph.get_all_src_dict()[src].keys():
                ed_dict = {"src": src, "w": self.__graph.get_edge_weigth(src, dest), "dest": dest}
                dictionary["Edges"].append(ed_dict)
        dictionary["Nodes"] = []
        for node in self.__graph.get_all_v().values():
            pos = "{},{},{}".format(node.get_location().get_x(), node.get_location().get_y(),
                                    node.get_location().get_z())
            id_node = node.get_ID()
            no_dict = {"pos": pos, "id": id_node}
            dictionary["Nodes"].append(no_dict)

        try:
            json_object = json.dumps(dictionary, indent=4)
            with open(file_name, 'w') as outfile:  # Open a file for writing
                outfile.write(json_object)
                # end = time.time()
                # print("the time it took for the function save_to_json to run is: {} sec.".format(end - begin))
                return True
        except Exception as e:
            print(e)
            # end = time.time()
            # print("the time it took for the function save_to_json to run is: {} sec.".format(end - begin))
            return False

    def Dijkstra(self, src) -> (list[int], list[int]):
        dist = {src: 0}
        for node in self.__graph.get_all_v().keys():
            if node == src:
                continue
            dist[node] = math.inf
        parantMap = {}
        for node in self.__graph.get_all_v().keys():
            parantMap[node] = None
        heap_queue = PriorityQueue()
        heap_queue.put((0, src))
        while not heap_queue.empty():
            v = heap_queue.get()
            if v[1] not in self.__graph.get_all_src_dict():
                break
            for neighbor in self.__graph.all_out_edges_of_node(v[1]).keys():
                old_dist = dist[neighbor]
                new_dist = dist[v[1]] + self.__graph.get_edge_weigth(v[1], neighbor)
                if new_dist < old_dist:
                    dist[neighbor] = new_dist
                    parantMap[neighbor] = v[1]
                    heap_queue.put((new_dist, neighbor))
        return parantMap, dist

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        # begin = time.time()
        if id1 not in self.__graph.get_all_v() or id2 not in self.__graph.get_all_v():
            # end = time.time()
            # print("the time it took for the function shortest_path to run is: {} sec.".format(end - begin))
            return math.inf, []
        if id1 is id2:
            end = time.time()
            # print("the time it took for the function shortest_path to run is: {} sec.".format(end - begin))
            # return 0, [id1]
        parent, shortest_path_dist = self.Dijkstra(id1)
        if shortest_path_dist[id2] == math.inf:
            end = time.time()
            # print("the time it took for the function shortest_path to run is: {} sec.".format(end - begin))
            # return math.inf, []
        path = []
        if id2 in parent:
            v = id2
            while v is not None:
                path.append(v)
                v = parent[v]
        # end = time.time()
        # print("the time it took for the function shortest_path to run is: {} sec.".format(end - begin))
        return shortest_path_dist[id2], path[::-1]

    def centerPoint(self) -> (int, float):
        # begin = time.time()
        if not self.isConnected():
            # end = time.time()
            # print("the time it took for the function centerPoint to run is: {} sec.".format(end - begin))
            return None, math.inf
        min_dist = sys.maxsize
        index_of_center = -1
        for node in self.__graph.get_all_v().keys():
            tmp_dist = self._find_max_dist(node)
            if tmp_dist < min_dist:
                min_dist = tmp_dist
                index_of_center = node
        # end = time.time()
        # print("the time it took for the function centerPoint to run is: {} sec.".format(end - begin))
        return index_of_center, min_dist

    def _find_max_dist(self, cuur) -> float:
        max_dist = -sys.maxsize - 1
        for node in self.__graph.get_all_v().keys():
            shortest_path = self.shortest_path(cuur, node)[0]
            if shortest_path > max_dist:
                max_dist = shortest_path
        return max_dist

    def isConnected(self) -> bool:
        for node in self.__graph.get_all_v().keys():
            dist = self.Dijkstra(node)[1]
            for d in dist.values():
                if d == math.inf:
                    return False
        return True

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        # begin = time.time()
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
            # end = time.time()
            # print("the time it took for the function TSP to run is: {} sec.".format(end - begin))
            return [], math.inf
        # end = time.time()
        # print("the time it took for the function TSP to run is: {} sec.".format(end - begin))
        return path, sum_weight

    def plot_graph(self) -> None:
        import networkx as nx
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(9, 6))
        ax = fig.add_subplot()
        ax.set_title('Graph Show')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        x_lable = []
        y_lable = []
        G = nx.DiGraph()
        for src in self.__graph.get_all_src_dict().keys():
            for dest in self.__graph.get_all_src_dict()[src]:
                G.add_edges_from([(src, dest)], weight=self.__graph.get_all_src_dict()[src][dest])
        initialpos = {}
        for node in self.__graph.get_all_v().values():
            x = node.get_location().get_x()
            x_lable.append(x)
            y = node.get_location().get_y()
            y_lable.append(y)
            initialpos[node.get_ID()] = (x, y)
        node_list = initialpos.keys()
        isPosExists = True
        for pos in initialpos.values():
            if pos == (0, 0):
                isPosExists = False
        if isPosExists:
            ax.set_xlim([self._find_min_x_or_y(x_lable), self._find_max_x_or_y(x_lable)])
            ax.set_ylim([self._find_min_x_or_y(y_lable), self._find_max_x_or_y(y_lable)])
            pos = nx.spring_layout(G, pos=initialpos, fixed=node_list)
        else:
            pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=100)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos, font_color='black', font_size=5)
        plt.show()

    def _find_min_x_or_y(self, val_lable: list) -> float:
        min_val = sys.maxsize
        for val in val_lable:
            if val < min_val:
                min_val = val
        return (min_val-0.00025)

    def _find_max_x_or_y(self, val_lable: list) -> float:
        max_val = -sys.maxsize - 1
        for val in val_lable:
            if val > max_val:
                max_val = val
        return (max_val+0.00025)




