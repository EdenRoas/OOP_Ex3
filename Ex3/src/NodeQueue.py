class NodeQueue:

    def __init__(self, dist: float, id_node: int):
        self.dist = dist
        self.node_id = id_node

    def get_dist(self):
        return self.dist

    def get_id(self):
        return self.node_id