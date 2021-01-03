class LinkedList:
    class node:
        def __init__(self, value = None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.lenght = 0

    def append(self, value):

        new_node = self.node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return self

    def prepend(self, value):

        new_node = self.node(value)
        new_node.next = self.head
        self.head = new_node
        self.lenght += 1
        return self

    def insert(self, index, value):

        if isinstance(index, int):

            if index >= self.lenght:
                return self.append(value)

            new_node = self.node(value)
            leader = self.traverse_to_index(index - 1)
            next_node = leader.next
            leader.next = new_node
            new_node.next = next_node
            return self
        else:
            print('Index must be an integer!')
            return

    def remove(self, index):

        if isinstance(index, int):
            if self.lenght <= index or index < 0:
                print('Index must be smaller than list lenght and greater than 0!')
                return
            elif index == 0:
                self.head = self.head.next
                self.lenght -= 1
                return self
            item = self.traverse_to_index(index - 1)
            remove_item = item.next
            item.next = remove_item.next
            self.lenght -= 1
            return self
        else:
            print('Index must be an integer!')
            return

    def lookup(self, value):

        counter = 0
        current_node = self.head
        while counter < self.lenght:
            if current_node.value == value:
                return counter, value
            counter += 1
            current_node = current_node.next
        return

    def traverse_to_index(self, index):

        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self

    def print(self):

        if self.head is None:
            print('Linked list is empty')
            return
        else:
            array = []
            current_node = self.head
            while current_node:
                array.append(current_node.value)
                current_node = current_node.next
            print(array)

    def __len__(self):
        return self.lenght

numbers = LinkedList()
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.print()
numbers.remove(2)
numbers.print()