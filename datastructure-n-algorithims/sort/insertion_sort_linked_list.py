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

    def insertion_sort(self):
        """
        Your approach: separate sorted and unsorted lists
        """
        if self.length < 2 or self.head is None:
            return

        # Initialize empty sorted list
        sorted_head = None
        sorted_tail = None

        current = self.head

        while current:
            next_node = current.next

            # Case 1: First element in sorted list
            if sorted_head is None:
                sorted_head = current
                sorted_tail = current
                current.next = None

            # Case 2: Insert at beginning (smaller than head)
            elif current.value <= sorted_head.value:
                current.next = sorted_head
                sorted_head = current

            # Case 3: Insert at end (larger than tail)
            elif current.value >= sorted_tail.value:
                sorted_tail.next = current
                sorted_tail = current
                current.next = None

            # Case 4: Insert in middle
            else:
                prev = sorted_head
                while prev.next and prev.next.value < current.value:
                    prev = prev.next

                current.next = prev.next
                prev.next = current

            current = next_node

        # Update original list pointers
        self.head = sorted_head
        self.tail = sorted_tail


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
4->2->6->5->1->3

2->4->5->6
1->3

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
