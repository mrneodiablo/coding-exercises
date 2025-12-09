class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        if values:
            print(" -> ".join(values))
        else:
            print("empty")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def selection_sort(self):
        if self.length < 2 or self.head is None:
            return

        current = self.head

        for i in range(self.length - 1):
            min_node = current
            search_node = current.next

            # Find minimum in remaining unsorted portion
            for _ in range(i + 1, self.length):
                if search_node.value < min_node.value:
                    min_node = search_node
                search_node = search_node.next

            # Swap values if a smaller element was found
            if min_node != current:
                current.value, min_node.value = min_node.value, current.value

            current = current.next


# Test Cases:
# -----------------------------------

# Test 1: Empty list
print("Test 1: Empty list")
ll1 = LinkedList(5)
ll1.head = None
ll1.length = 0
ll1.selection_sort()
ll1.print_list()  # Should print: empty
print("-" * 30)

# Test 2: Single element
print("Test 2: Single element")
ll2 = LinkedList(5)
ll2.selection_sort()
ll2.print_list()  # Should print: 5
print("-" * 30)

# Test 3: Already sorted list
print("Test 3: Already sorted list")
ll3 = LinkedList(1)
ll3.append(2)
ll3.append(3)
ll3.selection_sort()
ll3.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 4: Reverse order
print("Test 4: Reverse order")
ll4 = LinkedList(3)
ll4.append(2)
ll4.append(1)
ll4.selection_sort()
ll4.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 5: Random order
print("Test 5: Random order")
ll5 = LinkedList(2)
ll5.append(1)
ll5.append(3)
ll5.selection_sort()
ll5.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 6: List with duplicates
print("Test 6: List with duplicates")
ll6 = LinkedList(3)
ll6.append(2)
ll6.append(2)
ll6.append(1)
ll6.append(3)
ll6.selection_sort()
ll6.print_list()  # Should print: 1 -> 2 -> 2 -> 3 -> 3
print("-" * 30)
