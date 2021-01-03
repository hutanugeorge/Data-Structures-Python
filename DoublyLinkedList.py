class DoublyLinkedList:
    class node:
        def __init__(self, value = None):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):

        self.head = None
        self.tail = self.head
        self.lenght = 0

    def append(self, value):

        new_node = self.node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.prev = self.head
            self.lenght += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.lenght += 1
        return self

    def prepend(self, value):

        new_node = self.node(value)
        if not self.head:
            print("You can't prepend on a empty list")
            return
        self.head.prev = new_node
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
            new_node.prev = leader
            next_node.prev = new_node
            self.lenght += 1
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
                next_item = self.head.next
                next_item.prev = None
                self.head = next_item
                self.lenght -= 1
                return self
            if index == self.lenght-1:
                prev_tail = self.tail.prev
                prev_tail.next = None
                self.tail = prev_tail
                self.lenght -= 1
                return self
        item = self.traverse_to_index(index-1)
        remove_item = item.next
        item.next = remove_item.next
        item.next.prev = remove_item.prev
        self.lenght -= 1
        return self

    def traverse_to_index(self, index):

        current_node = self.head
        counter = 0
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def __len__(self):
        return self.lenght

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


numbers = DoublyLinkedList()

numbers.append(3)
numbers.prepend(1)
numbers.append(4)
numbers.append(12)
numbers.remove(0)
numbers.print()

