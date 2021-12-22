from unittest import TestCase
from src.Point3D import Point3D
from src.NodeData import NodeData
from src.DiGraph import DiGraph

class TestDiGraph(TestCase):
    id1 = 0
    id2 = 1
    id3 = 2
    x1 = 35.18869800968523
    x2 = 35.187594216303474
    x3 = 35.19381366747377
    y1 = 32.104927164705884
    y2 = 32.10378225882353
    y3 = 32.102419275630254
    z = 0.0
    loc1 = Point3D(x=x1, y=y1, z=z)
    loc2 = Point3D(x=x2, y=y2, z=z)
    loc3 = Point3D(x=x3, y=y3, z=z)
    n1 = NodeData(id1, loc1)
    n2 = NodeData(id2, loc2)
    n3 = NodeData(id3, loc3)
    vertice_dict = [n1]
    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
