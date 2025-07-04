class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoubleLinkedList:
    def __init__(self, value=None):
        new_node = Node(value)
        new_node.previous = None
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.length += 1
        return True

    def pop(self) -> Node:
        if self.head is None:
            return None

        tmp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            tmp.previous = None
            self.tail.next = None
        self.length -= 1
        return tmp

    def pop_first(self) -> Node:
        if self.length == 0:
            return None

        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            tmp.next = None

        self.length -= 1
        return tmp

    def get(self, index) -> Node:
        # length is 7
        # index is 5
        # index_head = 0, index_tail = 6
        # cover edge cases first
        if self.length == 0 or index >= self.length:
            return None

        if self.length == 1:
            return self.head

        #
        #        length
        #  I----------------I
        #
        #  I------------I---I
        #             index
        if index < self.length / 2:
            node = self.head
            for _ in range(0, index, 1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.previous
        return node

    def set_value(self, value, index) -> bool:
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        next_node = self.get(index)
        previous_node = next_node.previous
        new_node = Node(value)

        # establish between left node and new node
        previous_node.next = new_node
        new_node.previous = previous_node

        # establish between right node and new node
        new_node.next = next_node
        next_node.previous = new_node
        self.length += 1

        return True

    def remove(self, index) -> bool:
        if index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        deleted_node = self.get(index)
        previous_node = deleted_node.previous
        next_node = deleted_node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        # delete memory
        deleted_node.next = None
        deleted_node.previous = None
        self.length -= 1
        return True

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True

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


if __name__ == "__main__":
    dll = DoubleLinkedList(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.print_linked_list()
    dll.remove(index=3)
    # print(dll.pop_first().value)

    dll.print_linked_list()
