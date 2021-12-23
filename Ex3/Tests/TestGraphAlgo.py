from unittest import TestCase
from src.GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):

    g_algo = GraphAlgo()
    g_algo.get_graph().addNode(0)

    g_algo.get_graph().addNode(1)
    g_algo.get_graph().addNode(2)
    g_algo.get_graph().addEdge(0, 1, 1)
    g_algo.get_graph().addEdge(1, 2, 4)

    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.assertEqual((1, [0, 1]), self.g_algo.shortestPath(0, 1))
        # self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
