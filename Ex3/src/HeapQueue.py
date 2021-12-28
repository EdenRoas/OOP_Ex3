from NodeQueue import NodeQueue


class HeapQueue:

    def __init__(self):
        self.heap_queue = []
        self.size = 0

    def push(self, new_node: NodeQueue):
        self.heap_queue.append(new_node)
        self.size += 1

    def pop(self, node: NodeQueue):
        if self.is_empty():
            print("out of nodes!")
            return
        self.heap_queue.remove(node)
        self.size -= 1

    def head(self):
        return self.heap_queue[0]

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def get_minimum(self):
        if self.is_empty():
            return -1
        minimum_dist = self.heap_queue[0].get_dist()
        minimum_dist_id = self.heap_queue[0].get_id()
        if self.size == 1:
            return minimum_dist_id
        for node in self.heap_queue:
            if node.get_dist() < minimum_dist:
                minimum_dist = node.get_dist()
                minimum_dist_id = node.get_id()
        node_to_pop = NodeQueue(minimum_dist, minimum_dist_id)
        self.pop(node_to_pop)
        return minimum_dist_id

