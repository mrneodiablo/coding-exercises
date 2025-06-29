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

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None

        step = 0
        tmp = self.head
        while step < index:
            tmp = tmp.next
            step += 1
        return tmp

    def has_loop(self) -> bool:
        slow = self.head
        fast = self.head

        while fast.next:
            fast = fast.next.next
            slow = slow.next

            # There are tail attribute of linked list with None
            if fast is None:
                return False

            if fast == slow:
                return True
        return False

    def print_list(self):
        if self.length == 0:
            print("None")
            return

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# setup linked list has loop
my_linked_list = LinkedList(4)
my_linked_list.append(Node(1))
my_linked_list.append(Node(3))
my_linked_list.append(Node(10))
# tmp = my_linked_list.get(3)
# tmp.next = my_linked_list.get(0)
print(my_linked_list.has_loop())
