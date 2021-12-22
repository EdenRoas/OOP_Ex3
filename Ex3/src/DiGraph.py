from GraphInterface import GraphInterface
from NodeData import NodeData
from src.Point3D import Point3D


class DiGraph(GraphInterface):

    def __init__(self):
        self._mc = 0
        self._vertices_dict : {int : NodeData} = {}
        self._src_edge_dict = {}
        self._dest_edge_dict = {}

    def v_size(self) -> int:
        return len(self._vertices_dict)

    def e_size(self) -> int:
        sum_of_edges = 0
        for e in self._src_edge_dict:
            sum_of_edges += len(e)
        return sum_of_edges

    def get_all_v(self) -> dict:
        return self._vertices_dict

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._dest_edge_dict.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._src_edge_dict.get(id1)

    def get_mc(self) -> int:
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self._vertices_dict.keys():
            return False
        if id2 not in self._vertices_dict.keys():
            return False
        if id1 in self._src_edge_dict.keys():
            if id2 in self._src_edge_dict[id1].keys():
                return False
        if id2 in self._dest_edge_dict.keys():
            if id1 in self._dest_edge_dict[id2].keys():
                return False
        if id1 not in self._src_edge_dict.keys():
            self._src_edge_dict[id1] = {}
        self._src_edge_dict[id1][id2] = weight
        if id2 not in self._dest_edge_dict.keys():
            self._dest_edge_dict[id2] = {}
        self._dest_edge_dict[id2][id1] = weight
        self._vertices_dict.get(id1).update_neighbors_list(self._vertices_dict.get(id2))
        self._mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._vertices_dict.keys():
            return False
        if pos == None:
            new_node = NodeData(node_id, Point3D(0, 0, 0))
        else:
            new_node = NodeData(node_id, Point3D(pos[0], pos[1], pos[2]))
        self._vertices_dict[node_id] = new_node
        self._mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._vertices_dict.keys():
            return False
        del self._vertices_dict[node_id]
        for e in self._dest_edge_dict[node_id]:
            del self._src_edge_dict[e][node_id]
        del self._dest_edge_dict[node_id]
        for e in self._src_edge_dict[node_id]:
            del self._dest_edge_dict[e][node_id]
        del self._src_edge_dict[node_id]
        for e in self._dest_edge_dict[node_id]:
            e.remove_from_neighbors_list(self._vertices_dict.get(node_id))
        self._mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._vertices_dict.keys():
            return False
        if node_id2 not in self._vertices_dict.keys():
            return False
        if node_id2 not in self._src_edge_dict[node_id1].keys():
            return False
        if node_id1 not in self._dest_edge_dict[node_id2].keys():
            return False
        del self._src_edge_dict[node_id1][node_id2]
        del self._dest_edge_dict[node_id2][node_id1]
        self._vertices_dict.get(node_id1).remove_from_neighbors_list(self._vertices_dict.get(node_id2))
        return True