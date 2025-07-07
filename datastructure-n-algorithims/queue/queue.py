class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value) -> bool:
        new_node = Node(value)

        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Node:
        if self.first is None:
            return None

        out = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            out.next = None
        self.length -= 1
        return out

    def print_queue(self):
        if self.first is None:
            return
        head = self.first
        out = []
        for _ in range(self.length):
            out.insert(0, head.value)
            head = head.next
        print(out)


if __name__ == "__main__":
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.print_queue()
    print("_________")
    print(q.dequeue().value)
    print(q.dequeue().value)
    print(q.dequeue().value)
    q.print_queue()
