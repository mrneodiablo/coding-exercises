class Node:
    def __init__(self, value, next: object = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def prepend(self, new_node: Node) -> bool:
        new_node.next = self.head
        self.head = new_node
        self.length = self.length + 1
        return True

    def append(self, new_node: Node) -> bool:
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def pop_last(self) -> Node:
        if self.head is None:
            return None

        if self.head == self.tail and self.head is not None:
            self.head = None
            self.tail = None
            return self.head

        ##
        tmp = self.head
        while tmp.next != self.tail:
            tmp = tmp.next
        result = self.tail
        self.tail = tmp
        tmp.next = None
        return result

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            del self.head
        else:
            self.head = self.head.next
        self.length -= 1
        return None

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None

        step = 0
        tmp = self.head
        while step < index:
            tmp = tmp.next
            step += 1
        return tmp

    def set(self, index: int, value):
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return tmp
        return None

    def print_list(self):
        if self.length == 0:
            print("None")
            return

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(Node(1))
my_linked_list.append(Node(3))
my_linked_list.append(Node(10))

print(my_linked_list.print_list())

my_linked_list.set(2, 10)
print(my_linked_list.print_list())
