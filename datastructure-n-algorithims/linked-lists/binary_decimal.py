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


def binart_to_decimal(linked_list: LinkedList) -> int:
    # first initial idea
    # data = {}
    # output = 0
    # ll = linked_list.head
    # counter = 0
    # while ll:
    #     if ll.value != 0:
    #         data[counter] = 0
    #     else:
    #         data[counter] = -1

    #     for k, v in data.items():
    #         if k == counter:
    #             pass
    #         else:
    #             if v != -1:
    #                 data[k] += 1

    #     counter += 1
    #     ll = ll.next

    # for _, v in data.items():
    #     if v != -1:
    #         output += 2**v

    # return output

    # Second idea
    # revert LinkedList then proceed  as usual
    # 1101 --> 1011
    # counter = 0
    # linked_list.reverse()
    # ll = linked_list.head
    # output = 0
    # while ll:
    #     if ll.value != 0:
    #         output += 2**counter
    #     counter += 1
    #     ll = ll.next

    # return output

    # third idea:
    # each step we jump we will double counted in previous steps:
    #   if value is 1:   out = 2*out + 1
    #   if value is 2:   out = 2*out
    # ý tưởng của số nhị phân khi duyệt từ trái qua phải là:
    # mỗi lần thêm 1 số bên phải thì số đầu sẽ x2 + số bên phải:
    # 1 --> giá trị sẽ là 1,
    # 10 --> 1*2 + 0
    # 101 --> (1*2 + 0)*2 + 1
    # tương tự như số thập phân
    # giả sử ta có 2, khi thêm 5 bên phải thành 25 --> 2*10 + 5
    output = 0
    ll = linked_list.head
    while ll:
        if ll.value == 1:
            output = 2 * output + 1
        else:
            output = 2 * output
        ll = ll.next
    return output


my_linked_list = LinkedList(1)
my_linked_list.append(Node(1))
my_linked_list.append(Node(1))
my_linked_list.append(Node(1))

print(my_linked_list.print_list())

print(binart_to_decimal(my_linked_list))
