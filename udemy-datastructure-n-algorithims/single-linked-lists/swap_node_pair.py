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

    def append(self, new_node: Node) -> bool:
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def print_list(self):
        if self.length == 0:
            return

        temp = self.head
        out = []
        while temp is not None:
            out.append(temp.value)
            temp = temp.next
        print(out)

    def swap_pairs(self) -> bool:
        # first thing first
        # Create dummy node dummy()->self.head
        # previous = dummy ,
        # first = previous.next,
        # second = previous.next.next
        # ==> check if previous.next and previous.next.next
        # tmp = second.next
        # previous.next = second
        # second.next = first
        # first.next = tmp
        # previous = previous.next.next

        if self.head is None:
            return False

        dummy = Node(0)
        dummy.next = self.head

        previous = dummy
        while previous.next and previous.next.next:

            first = previous.next
            second = previous.next.next
            tmp = second.next
            previous.next = second
            second.next = first
            first.next = tmp
            previous = previous.next.next
        self.head = dummy.next
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(Node(2))
my_linked_list.append(Node(3))
my_linked_list.append(Node(4))
my_linked_list.append(Node(5))


print(my_linked_list.print_list())
my_linked_list.swap_pairs()
print(my_linked_list.print_list())
