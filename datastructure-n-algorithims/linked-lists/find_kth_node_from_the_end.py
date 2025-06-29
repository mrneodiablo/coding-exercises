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


def find_kth_from_end(linked_list: LinkedList, k: int) -> Node:
    """
    The ideal is:
    - List = [6 5 4 3 2 1]
    - k = 5
    - fast poiter will check if K > length of Linked List
        [ 6 5 4 3 2 1]
          S       F
    - IF K <= length:
        - we want to find K from the end of list to head basically
            - ==> Length (List) - k = 1
            ==> so, k stands at 1 from head
        - In the other words after step checking K with length,
          we jumps Head umtil Tail got None
          [ 9 8 7 6 5 4 3 2 1]
          k = 4
          1: [ 9 8 7 6 5 4 3 2 1]
               S     F
          2: [ 9 8 7 6 5 4 3 2 1]
                         S     F



    """

    slow = linked_list.head
    fast = linked_list.head

    for _ in range(k + 1):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


my_linked_list = LinkedList(4)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(11)
my_linked_list.append(12)


my_linked_list.print_list()

print(f"The midle of node value: {find_kth_from_end(my_linked_list, 5).value}")
