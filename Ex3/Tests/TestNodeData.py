from unittest import TestCase
from src.Point3D import Point3D
from src.NodeData import NodeData


class TestNodeData(TestCase):
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

    def test_get_id(self):
        self.assertEqual(self.id1, self.n1.get_ID())
        self.assertEqual(self.id2, self.n2.get_ID())
        self.assertEqual(self.id3, self.n3.get_ID())

    def test_get_location(self):
        self.assertEqual(self.loc1.__dict__, self.n1.get_location().__dict__)
        self.assertEqual(self.loc2.__dict__, self.n2.get_location().__dict__)
        self.assertEqual(self.loc3.__dict__, self.n3.get_location().__dict__)
