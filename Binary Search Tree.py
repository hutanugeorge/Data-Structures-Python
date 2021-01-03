class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            next_node = self.root

            while True:
                if next_node.value > new_node.value:
                    if not next_node.left:
                        next_node.left = new_node
                        break
                    next_node = next_node.left
                elif next_node.value < new_node.value:
                    if not next_node.right:
                        next_node.right = new_node
                        break
                    next_node = next_node.right
                else:
                    raise ValueError('You can\'t insert two nodes with the same value.')
        return self

    def lookup(self, value):

        current_node = self.root

        while current_node:
            if current_node.value == value:
                return True
            elif current_node.value < value:
                current_node = current_node.right
            elif current_node.value > value:
                current_node = current_node.left
        return False

    def remove(self, value):

        # Search node
        current_node = self.root
        parent_node = None
        direction = None
        left_node = None

        while True:
            if current_node.value < value:
                parent_node = current_node
                direction = 'right'
                current_node = current_node.right

            elif current_node.value > value:
                parent_node = current_node
                direction = 'left'
                current_node = current_node.left

            else:
                # Find value!!

                # Check if it is a leaf
                if self._leaf(current_node):
                    if direction == 'left':
                        parent_node.left = None

                    else:
                        parent_node.right = None
                    break


                # Check if it has a child
                elif self._one_child(current_node):

                    if direction == 'left':
                        if self._have_left_child(current_node):
                            parent_node.left = current_node.left
                        else:
                            parent_node.left = current_node.right
                    else:
                        if self._have_left_child(current_node):
                            parent_node.right = current_node.left
                        else:
                            parent_node.right = current_node.right

                    break


                # Check if it has 2 children
                elif self._2_children(current_node):
                    left_node = current_node.left
                    print(left_node.value, 'left')
                    print(parent_node.value, 'parent')
                    current_node = current_node.right

                    if self._leaf(current_node):
                        replace_node = current_node
                        break

                    else:
                        right_node = current_node
                        print(right_node.value, 'right')
                        replace_node = self._find_min_right(current_node)

                        if direction == 'left':
                            parent_node.left = replace_node
                            replace_node.right = right_node
                            replace_node.left = left_node
                            break

                        else:
                            parent_node.right = replace_node
                            replace_node.right = right_node
                            replace_node.left = left_node
                            break

    def _leaf(self, node):
        return node.left is None and node.right is None

    def _one_child(self, node):
        return node.left is None and isinstance(node.right.value, int) or \
               isinstance(node.left.value, int) and node.right is None

    def _2_children(self, node):
        return isinstance(node.left.value, int) and isinstance(node.right.value, int)

    def _have_right_child(self, node):
        try:
            return isinstance(node.right.value, int)
        except:
            return False

    def _have_left_child(self, node):
        try:
            return isinstance(node.left.value, int)
        except:
            return False

    def _find_min_right(self, node):

        if self._leaf(node):
            return node

        elif self._have_left_child(node):
            prev_node = node
            node = node.left

            if self._leaf(node):
                prev_node.left = None
                return node

            elif self._have_right_child(node) and not self._have_left_child(node):
                prev_node.left = node.right
                return node

            else:
                prev_node = node
                node = node.left
                return self._find_min_right(node)

        else:
            return node


numbers = BinarySearchTree()
numbers.insert(30)
numbers.insert(20)
numbers.insert(40)
numbers.insert(25)
numbers.insert(10)
numbers.insert(5)
numbers.insert(46)
numbers.insert(35)
numbers.insert(36)
numbers.insert(50)
numbers.insert(45)
numbers.insert(24)
numbers.insert(44)
numbers.insert(41)
numbers.insert(42)
numbers.remove(40)
numbers.lookup(5)
