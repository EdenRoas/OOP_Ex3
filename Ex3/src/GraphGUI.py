# # from GraphAlgo import GraphAlgo
# import sys
#
# import pygame as pg
# # from pygame.examples.headless_no_windows_needed import screen
# # from src.GraphAlgo import GraphAlgo
# from src.GraphAlgoInterface import GraphAlgoInterface
#
# pg.font.init()
#
#
# class GraphGUI:
#
#     def _init_(self):
#         self.algo = GraphAlgoInterface
#
#     def run_gui(self, graph_algo: GraphAlgoInterface):
#         pg.init()
#         self.algo = graph_algo
#         scr = pg.display.set_mode((1000, 700))
#         pg.display.set_caption("Graph Plot")
#         running = True
#         while running:
#             for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                     running = False
#                 if event.type == pg.MOUSEBUTTONDOWN:
#                     if pg.mouse.get_pos() >= (850, 210 + yd):
#                         if pg.mouse.get_pos() <= (850 + xd, 210):
#                             self.draw_graph(scr)
#             scr.fill((255, 255, 255))
#             load_button, xl, yl = self.button(scr, (850, 90), "load")
#             save_button, xs, ys = self.button(scr, (850, 150), "save")
#             draw_button, xd, yd = self.button(scr, (850, 210), "draw")
#             pg.display.update()
#         pg.quit()
#         sys.exit()
#
#     def button(self, screen, position, text):
#         font = pg.font.SysFont("Arial", 25)
#         text_render = font.render(text, True, (0, 0, 0))
#
#         x, y, w, h = text_render.get_rect()
#         x, y = position
#         pg.draw.rect(screen, (131, 139, 139), (x, y, w, h))
#         return screen.blit(text_render, (x, y)), x, y
#
#     def draw_graph(self, screen):
#         nodes_dict = self.algo.get_graph().get_all_v()
#         for node in nodes_dict.values():
#             pg.draw.circle(screen, (4, 42, 219), (node.get_location().get_x(), node.get_location().get_y(),
#                                                   node.get_location().get_z()), radius=5)
#
#
import sys
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab

# from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class GraphGUI:

    def __init__(self, graph_algo: GraphAlgo):
        self.algo = graph_algo
        self.width = 1000
        self.height = 700

    def run_gui(self):
        self.draw_graph()

    def draw_graph(self):
        G = nx.DiGraph()
        all_edges = []
        for src in self.algo.get_graph().get_all_src_dict().keys():
            for dest in self.algo.get_graph().get_all_src_dict()[src]:
                all_edges.append((src, dest))

        G.add_edges_from(all_edges, weight=1)
        # G.add_edges_from([('D', 'A'), ('D', 'E'), ('B', 'D'), ('D', 'E')], weight=2)
        # G.add_edges_from([('B', 'C'), ('E', 'F')], weight=3)
        # G.add_edges_from([('C', 'F')], weight=4)

        # val_map = {'A': 1.0,
        #            'D': 0.5714285714285714,
        #            'H': 0.0}

        # values = [val_map.get(node, 0.45) for node in G.nodes()]
        # edge_labels = dict([((u, v,), d['weight'])
        #                     for u, v, d in G.edges(data=True)])
        # red_edges = [('C', 'D'), ('D', 'A')]
        # edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

        pos = nx.spring_layout(G)
        # print(pos)
        # minX = self.get_min_x()
        # minY = self.get_min_y()
        # maxX = self.get_max_x()
        # maxY = self.get_max_y()

        # pos = {}
        # for node in self.algo.get_graph().get_all_v().values():
        #     x = int((((node.get_location().get_x() - minX) * (self.width - 100)) / (maxX - minX + 1)) + 15)
        #     y = int((((node.get_location().get_y() - minY) * (self.height - 150)) / (maxY - minY + 1)) + 25)
        #     pos[node.get_ID()] = (x, y)
        nx.draw_networkx_nodes(G, pos, node_size=100)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black')
        nx.draw_networkx_labels(G, pos)
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        # nx.draw(G, pos, node_color=values, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
        pylab.show()

    def get_min_x(self):
        minx = sys.maxsize
        for node in self.algo.get_graph().get_all_v().values():
            if node.get_location().get_x() < minx:
                minx = node.get_location().get_x()
        return minx

    def get_min_y(self):
        miny = sys.maxsize
        for node in self.algo.get_graph().get_all_v().values():
            if node.get_location().get_y() < miny:
                miny = node.get_location().get_y()
        return miny

    def get_max_x(self):
        maxx = -sys.maxsize - 1
        for node in self.algo.get_graph().get_all_v().values():
            if node.get_location().get_x() > maxx:
                maxx = node.get_location().get_x()
        return maxx

    def get_max_y(self):
        maxy = -sys.maxsize - 1
        for node in self.algo.get_graph().get_all_v().values():
            if node.get_location().get_y() > maxy:
                maxy = node.get_location().get_y()
        return maxy

# class draw_graph:
#
#     def __init__(self, graph: DiGraph):
#         self.graph = graph
#         self.minX = sys.maxsize
#         self.maxX = -sys.maxsize - 1
#         self.minY = sys.maxsize
#         self.maxY = -sys.maxsize - 1
#
#
#     def getMinX(self):
#         for node in self.graph.get_all_v().values():
#             if node.get_location().get_x() < self.minX:
#                 self.minX = node.get_location().get_x()
#
#     def getMinY(self):
#         pass






