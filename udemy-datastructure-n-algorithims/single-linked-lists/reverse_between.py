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

    def reverse_between_head_insertion(self, first_index, second_index):
        """
        Reverses a portion of the linked list between two given indices using
        head insertion technique.
        This method reverses the nodes in the linked list from
        position first_index to
        second_index (inclusive) by repeatedly moving nodes to
        the front of the sublist
        using a head insertion approach.
        Args:
            first_index (int): The starting index of
            the portion to reverse (0-based)

            second_index (int): The ending index of
            the portion to reverse (0-based)
        Returns:
            None: The method modifies the linked list in-place
        Time Complexity: O(n) where n is the position of second_index
        Space Complexity: O(1) as only a constant amount of extra space is used
        Example:
            Original list: 1 -> 2 -> 3 -> 4 -> 5
            reverse_between_head_insertion(1, 3)
            Result: 1 -> 4 -> 3 -> 2 -> 5
        """

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # get the current first_index
        for _ in range(first_index):
            prev = prev.next

        curr = prev.next
        for _ in range(second_index - first_index):
            to_move = curr.next
            curr.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        self.head = dummy.next

    def print_list(self):
        if self.length == 0:
            return

        temp = self.head
        out = []
        while temp is not None:
            out.append(temp.value)
            temp = temp.next
        print(out)


def _reverse_list(head: Node) -> Node:
    prev = None
    curr = head
    tmp = None  # luu gia tri de nhay tiep
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    head = prev
    return head


def _print_list(linked_list: LinkedList):
    if linked_list.length == 0:
        return

    temp = linked_list.head
    out = []
    while temp is not None:
        out.append(temp.value)
        temp = temp.next
    print(out)


def _reverse_between(
    linked_list: LinkedList, first_index=0, second_index=2
) -> LinkedList:
    """
    Reverse nodes of a linked list between two given indices.
    Args:
        linked_list (LinkedList): The linked list to modify
        first_index (int, optional): Starting index of the range to reverse.
        Defaults to 0.

        second_index (int, optional): Ending index of the range to reverse.
        Defaults to 2.
    Returns:
        LinkedList: The modified linked list with reversed section,
        or False if list length <= 1
    Example:
        Given linked list: 1->2->3->4->5 and first_index=1, second_index=3
        Result: 1->4->3->2->5
    Note:
        - Uses 0-based indexing
        - Creates a dummy node to simplify edge cases
        - Modifies the original linked list in place
        - Returns False for lists with length <= 1
    """
    if linked_list.length <= 1:
        return False

    # create dummy Node
    dummy = Node(0, next=linked_list.head)
    prev = dummy

    # Step 1: đi đến node trước đoạn cần đảo
    for _ in range(first_index):
        prev = prev.next

    start_node = prev.next
    tail = start_node
    # Step 2: đi đến cuối đoạn cần đảo
    for _ in range(second_index - first_index):
        tail = tail.next

    node_after = tail.next
    tail.next = None  # Tách đoan

    # revert list
    reversed_head = _reverse_list(start_node)

    prev.next = reversed_head
    start_node.next = node_after
    linked_list.head = dummy.next
    return linked_list


my_linked_list = LinkedList(1)
my_linked_list.append(Node(2))
my_linked_list.append(Node(3))
my_linked_list.append(Node(4))
my_linked_list.append(Node(5))
my_linked_list.print_list()
my_linked_list.reverse_between_head_insertion(first_index=0, second_index=1)
my_linked_list.print_list()

# _print_list(_reverse_between(my_linked_list,first_index=1,second_index=4))
# print(my_linked_list.print_list())
# # my_linked_list.reverse()
# my_linked_list.reverse_between(first_index=1, second_index=3)
# print(my_linked_list.print_list())
