from typing import List

from src.Point3D import Point3D


class NodeData:

    def __init__(self,  node_id: int, location: Point3D):
        self.__id = node_id
        self._location = Point3D(location.get_x(), location.get_y(), location.get_z())
        self._neighbors_list = List[NodeData]

    def get_ID(self) -> int:
        return self.__id

    def get_location(self) -> Point3D:
        return self._location

    def update_neighbors_list(self, neighbor) -> None:
        self._neighbors_list.append(neighbor)

    def remove_from_neighbors_list(self, neighbor) -> None:
        self._neighbors_list.remove(neighbor)

    def get_neighbors_list(self):
        return self._neighbors_list
