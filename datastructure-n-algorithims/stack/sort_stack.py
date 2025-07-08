class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


def sort_stack(in_stack: Stack) -> Stack:
    # in_stack: [ 3 1 5 4 2]
    # tmp = 1
    # sorted_descending_stack = []
    # thủ thuật này tương tự như việc tìm số lớn nhất trong dãy
    # in_stack append vào sorted_descending_stack
    # sau đó tìm số lớn nhì kiểu vầy là thao tác trên mảng

    # đối với thao tác trên stack, so sánh số đầu peek
    # của sorted_descending_stack với số tmp,
    # đại khái là kiểm tra dố tmp co phải
    # là số lớn nhất trong mảng sorted_descending_stack không,
    # nếu không phải số lớn nhât
    sorted_descending_stack = Stack()
    while not in_stack.is_empty():
        tmp = in_stack.pop()
        while (
            not sorted_descending_stack.is_empty()
            and sorted_descending_stack.peek() > tmp
        ):
            in_stack.push(sorted_descending_stack.pop())

        sorted_descending_stack.push(tmp)
    return True


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
