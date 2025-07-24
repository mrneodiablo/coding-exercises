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

    def bubble_sort(self):
        if self.head is None:
            return False

        if self.length < 2:
            return True

        for i in range(self.length - 1, 0, -1):
            starter = self.head
            check_pre_list_sorted = i - 1
            for _ in range(i):
                if starter and starter.next:
                    if starter.value > starter.next.value:
                        starter.value, starter.next.value = (
                            starter.next.value,
                            starter.value,
                        )
                else:
                    check_pre_list_sorted -= 1
                starter = starter.next

            if check_pre_list_sorted == 0:
                return True

        return True


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
