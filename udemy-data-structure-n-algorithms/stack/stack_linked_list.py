class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value) -> bool:
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self) -> Node:
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next
        # detach node
        node.next = None
        self.height -= 1
        return node

    def print_stack(self):
        st = self.top
        if self.height != 0:
            for _ in range(self.height):
                print(st.value)
                st = st.next
        else:
            print(None)


if __name__ == "__main__":
    stack = Stack(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print("-------------")
    stack.pop()
    stack.print_stack()
