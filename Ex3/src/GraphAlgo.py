import sys
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface

class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.__graph = None

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

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


