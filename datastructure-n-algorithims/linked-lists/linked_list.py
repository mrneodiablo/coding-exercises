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

    def prepend(self, new_node: Node) -> bool:
        new_node.next = self.head
        self.head = new_node
        self.length = self.length + 1
        return True

    def append(self, new_node: Node) -> bool:
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def pop_last(self) -> Node:
        if self.head is None:
            return None

        if self.head == self.tail and self.head is not None:
            self.head = None
            self.tail = None
            return self.head

        ##
        tmp = self.head
        while tmp.next != self.tail:
            tmp = tmp.next
        result = self.tail
        self.tail = tmp
        tmp.next = None
        return result

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            del self.head
        else:
            self.head = self.head.next
        self.length -= 1
        return None

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None

        step = 0
        tmp = self.head
        while step < index:
            tmp = tmp.next
            step += 1
        return tmp

    def set(self, index: int, value):
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return tmp
        return None

    def insert(self, index: int, value) -> bool:
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(Node(value))
            return True

        if index == self.length:
            self.append(Node(value))
            return True

        pre = self.head
        count = 0
        while count < index - 1:
            count += 1
            pre = pre.next

        new_code = Node(value, pre.next)
        pre.next = new_code

        # another implement more simple, that will leverage existing function
        # tmp = self.get(index-1)
        # new_code = Node(value,self.get(index))
        # tmp.next = new_code

        self.length += 1
        return True

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.pop_first()
            return True

        if self.length - 1 == index:
            self.pop_last()
            return True

        previous = self.get(index - 1)
        previous.next = previous.next.next
        self.length -= 1
        return True

    def reverse(self) -> bool:
        if self.length <= 1:
            return True

        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def remove_duplicates(self) -> bool:
        # option 1: using a set (O(n))
        # if self.head is None:
        #     return False

        # check_value = set()
        # fast = self.head
        # previous = fast
        # while fast:
        #     if fast.value not in check_value:
        #         check_value.add(fast.value)
        #         previous = fast
        #     else:
        #         previous.next = fast.next
        #         self.length -= 1
        #     fast = fast.next

        # return True

        # option 2: using 2 loops (O(n^2))
        if self.head is None:
            return False
        slow = self.head
        fast = self.head

        while slow:
            fast = slow.next
            previous = slow
            while fast:
                if fast.value == slow.value:
                    previous.next = fast.next
                    self.length -= 1
                else:
                    previous = fast
                fast = fast.next
            slow = slow.next
        return True

    def print_list(self):
        output = []
        if self.length == 0:
            print("None")
            return

        temp = self.head
        while temp is not None:
            output.append(temp.value)
            temp = temp.next

        print(output)
