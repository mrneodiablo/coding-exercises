class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def find_middle_node(self) -> Node:
        """
        we aren't allowed for using length to find midle node
        the algorithm somehow allow for 1 loop
        """
        if self.head is None:
            return None

        fast = self.head
        slow = self.head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                break
        return slow

    def print_list(self):
        if self.length == 0:
            print("None")
            return

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(11)
my_linked_list.append(12)


my_linked_list.print_list()

#
print(f"The midle of node value: {my_linked_list.find_middle_node().value}")
