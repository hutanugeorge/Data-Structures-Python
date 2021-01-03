class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)

        if not self.top:
            self.top = new_node
            self.bottom = new_node
        else:
            next_elem = self.top
            self.top = new_node
            self.top.next = next_elem
        self.lenght += 1
        return self

    def pop(self):

        if not self.top:
            return None

        if self.lenght == 1:
            self.top = None
            self.bottom = None
            self.lenght -= 1
            return None

        holding_Pointer = self.top
        self.top = self.top.next
        self.lenght -= 1
        return holding_Pointer

    def is_empty(self):
        if self.lenght == 0:
            return True
        return False

    def print(self):
        lst = []
        counter = 0
        current_node = self.top
        while counter < self.lenght:
            lst.append(current_node.value)
            current_node = current_node.next
            counter += 1
        print(lst)


class StackArray:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        self.stack.pop()
        return self

    def print(self):
        print(self.stack)

