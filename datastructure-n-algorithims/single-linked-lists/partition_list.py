"""
Linked List Partition Algorithm

This module implements a partition function for linked lists.

Algorithm Overview:
Given a linked list and a partition value, rearrange the list so that:
- All nodes with values less than the partition value come first
- All nodes with values greater than or equal to the partition value come after

Example:
Original:  3 -> 8 -> 5 -> 10 -> 2 -> 1
Partition value: 5
Result:    3 -> 2 -> 1 -> 8 -> 5 -> 10
           (< 5)        (>= 5)

The algorithm uses two separate lists (smaller and larger)
and then connects them.
"""


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

    def partition_list(self, partition_value: int):
        """
        Partitions the linked list around a given value.
        All nodes with values less than partition_value come before
        all nodes with values greater than or equal to partition_value.

        Args:
            partition_value (int): The value to partition around

        Returns:
            bool: True if partition was successful
        """
        # Handle edge case: empty list
        if self.head is None:
            return True

        # Step 1: Create two separate lists
        # List 1: for values less than partition_value
        smaller_dummy = Node(0)  # Dummy head for smaller values
        smaller_tail = smaller_dummy

        # List 2: for values greater than or equal to partition_value
        larger_dummy = Node(0)  # Dummy head for larger/equal values
        larger_tail = larger_dummy

        # Step 2: Traverse original list and split nodes into two lists
        current = self.head
        while current:
            next_node = current.next  # Save next before we break the link

            if current.value < partition_value:
                # Add to smaller list
                smaller_tail.next = current
                smaller_tail = current
            else:
                # Add to larger/equal list
                larger_tail.next = current
                larger_tail = current

            # Break the link to avoid cycles
            current.next = None
            current = next_node

        # Step 3: Connect the two lists
        # smaller_list -> larger_list
        smaller_tail.next = larger_dummy.next

        # Step 4: Update the head to point to the new list
        # (skip the dummy node)
        self.head = smaller_dummy.next

        return True


# Example usage and testing
if __name__ == "__main__":
    # Create a linked list: 3 -> 8 -> 5 -> 10 -> 2 -> 1
    my_linked_list = LinkedList(3)
    my_linked_list.append(Node(8))
    my_linked_list.append(Node(5))
    my_linked_list.append(Node(10))
    my_linked_list.append(Node(2))
    my_linked_list.append(Node(1))

    print("Original list:")
    my_linked_list.print_list()  # [3, 8, 5, 10, 2, 1]

    print("\nPartitioning around value 5...")
    my_linked_list.partition_list(5)

    print("After partition (values < 5 come before values >= 5):")
    my_linked_list.print_list()  # Should be: [3, 2, 1, 8, 5, 10]
