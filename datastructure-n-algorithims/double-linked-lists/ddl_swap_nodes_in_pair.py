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

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):

        dummy = Node(0)
        dummy.next = self.head

        previous = dummy
        while previous.next and previous.next.next:
            first = previous.next
            second = previous.next.next

            # swap second by first
            first.next = second.next
            if first.next:
                first.next.prev = first

            # swap first by second
            second.next = first
            first.prev = second

            # Move second to before
            second.prev = previous
            previous.next = second

            previous = previous.next.next

        self.head = dummy.next

        if self.head:
            self.head.prev = None

        return True


if __name__ == "__main__":
    dll = DoublyLinkedList(3)
    for v in [8, 5, 10, 2]:
        dll.append(v)
    dll.print_linked_list()
    dll.swap_pairs()
    dll.print_linked_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
