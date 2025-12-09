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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        """
        Merges another sorted linked list with this
        linked list in sorted order.
        This method assumes both
        linked lists are already sorted in ascending order.
        """
        dummy = Node(0)
        dummy.next = self.head

        current = dummy
        l1_current = dummy.next
        l2_current = other_list.head

        while l1_current and l2_current:
            if l1_current.value < l2_current.value:
                current.next = l1_current
                l1_current = l1_current.next
            else:
                current.next = l2_current
                l2_current = l2_current.next
            current = current.next

        if l1_current:
            current.next = l1_current
        else:
            current.next = l2_current

        self.head = dummy.next
        self.length += other_list.length

        return True


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
    5
    6
    7
    8

"""
