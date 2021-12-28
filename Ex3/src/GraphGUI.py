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
import matplotlib as plt

from src.GraphAlgo import GraphAlgo


class GraphGUI:

    def __init__(self):
        self.algo = GraphAlgo()



