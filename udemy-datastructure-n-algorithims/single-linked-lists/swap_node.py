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

    def reverse(self):
        if self.length <= 1:
            return True

        temp = self.head
        self.head = self.tail
        self.tail = temp

        previous = None
        next = temp.next
        for _ in range(self.length):
            next = temp.next
            temp.next = previous
            previous = temp
            temp = next
        return True

    def swap_nodes(self, first_index: int, second_index: int) -> bool:
        # first_index, second_index that is increasemential number :
        # start from 0
        if (
            self.length <= 1
            or self.length <= second_index
            or first_index == second_index
        ):
            return False
        dummy = Node(0, next=self.head)
        prev_node_1 = None
        node_1 = None

        prev_node_2 = None
        node_2 = None

        counter = 0
        prev = dummy
        while prev.next:
            if counter == first_index:
                prev_node_1 = prev
                node_1 = prev.next
            if counter == second_index:
                prev_node_2 = prev
                node_2 = prev.next
            counter += 1
            prev = prev.next

        if not node_2 or not node_1:
            return False

        # xu ly 2 node lien ke nhau
        if second_index - first_index == 1:
            node_1.next = node_2.next
            node_2.next = node_1
            prev_node_1.next = node_2
        else:
            # luu gia tri tam next node 1
            tmp = node_1.next
            prev_node_1.next = node_2
            node_1.next = node_2.next
            prev_node_2.next = node_1
            node_2.next = tmp
        self.head = dummy.next
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(Node(2))
my_linked_list.append(Node(3))
my_linked_list.append(Node(4))
my_linked_list.append(Node(5))

print(my_linked_list.print_list())
# my_linked_list.reverse()
my_linked_list.swap_nodes(first_index=2, second_index=3)
print(my_linked_list.print_list())
