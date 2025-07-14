class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, parental_index) -> int:
        return 2 * parental_index + 1

    def _right_child(self, parental_index) -> int:
        return 2 * parental_index + 2

    def _parent(self, child_index) -> int:
        return (child_index - 1) // 2

    def _swap(self, index_node1, index_node2) -> bool:
        self.heap[index_node1], self.heap[index_node2] = (
            self.heap[index_node2],
            self.heap[index_node1],
        )
        return True

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if (self.heap[left_index] > self.heap[max_index]) and (
                left_index < len(self.heap)
            ):
                max_index = left_index

            if (self.heap[right_index] > self.heap[max_index]) and (
                right_index < len(self.heap)
            ):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while (current > 0) and (
            self.heap[current] > self.heap[self._parent(current)]
        ):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self) -> int:
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


if __name__ == "__main__":
    my_heap = MaxHeap()

    my_heap.insert(80)
    my_heap.insert(75)
    my_heap.insert(65)
    my_heap.insert(55)
    my_heap.insert(50)
    my_heap.insert(60)
    print(my_heap.heap)
    print("=================")
    my_heap.remove()
    print(my_heap.heap)
