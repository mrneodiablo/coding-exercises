class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def print_linked_list(self) -> str:
        tmp = self.head
        output_right_to_left = []
        output_left_to_right = []
        while tmp:
            output_right_to_left.append(tmp.value)
            output_left_to_right.insert(0, tmp.value)
            tmp = tmp.next
        print(f"right_left: {output_right_to_left}")
        print(f"left_right: {output_left_to_right}")

    def reverse_between(self, start_index, end_index) -> bool:
        if start_index < 0 or end_index >= self.length:
            return False

        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev = dummy

        for _ in range(start_index):
            prev = prev.next

        curr = prev.next
        for _ in range(end_index - start_index):
            to_move = curr.next
            curr.next = to_move.next
            if to_move.next:
                to_move.next.prev = curr
            to_move.next = prev.next
            prev.next.prev = to_move
            to_move.prev = prev
            prev.next = to_move

        self.head = dummy.next
        return True


if __name__ == "__main__":
    dll = DoublyLinkedList(3)
    for v in [8, 5, 10, 2, 1]:
        dll.append(v)
    dll.print_linked_list()
    dll.reverse_between(1, 4)
    dll.print_linked_list()
