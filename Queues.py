class Queue:
    class node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def enqueue(self, value):
        new_node = self.node(value)
        if not self.first and not self.last:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        return self

    def dequeue(self):

        if not self.first:
            return None

        if self.lenght == 1:
            self.first = self.last = None
            self.lenght = 0

        self.first = self.first.next
        self.lenght -= 1
        return self

    def peek(self):
        return self.first

    def is_empty(self):
        if self.lenght == 0:
            return True
        return False

    def print(self):
        lst = []
        counter = 0
        current_node = self.first
        while counter < self.lenght:
            lst.append(current_node.value)
            current_node = current_node.next
            counter += 1
        print(lst)
