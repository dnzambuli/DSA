class Node:
    def __init__(self, value):
        """
        Constructor for Node class for a doubly linked list
        :param value:
        """
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value = None):
        if value is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.size = 1

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += " " + str(current.value)
            current = current.next
        return string

    def __len__(self):
        return self.size

    def append(self, value) -> bool:
        """
        append a value to the end of the dll
        :param value:
        :return:
        """
        # edge case: empty dll
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # edge case: dll with content
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return True

    def pop(self) -> Node:
        """
        pop a value from the end of the dll
        :return Node:
        """
        # edge case: empty dll
        if self.size == 0:
            return None
        # edge case: dll has only one element
        temp = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        # edge case: the dll has other elements
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.size -= 1

        return temp

    def prepend(self, value) -> bool:
        """
        add an element at the start of the dll
        :param value:
        :return:
        """
        # edge case: add to an empty dll
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        # edge case: dll has elements
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return True

    def pop_first(self) -> Node:
        """
        pop a value from the beginning of the dll
        :return:
        """
        # edge case: empty dll
        if self.size == 0:
            return None
        temp = self.head
        # edge case: dll with only one element
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.size -= 1
        return temp

# run the first test

# ==========================
#
# Testing appenidng
#
# ==========================

test_empty = DoublyLinkedList()

print("empty dll: ", test_empty)

test_one_element = DoublyLinkedList(1)
print("one element dll: ", test_one_element)

# ==========================
#
# Testing pop
#
# ==========================

test_pop = DoublyLinkedList(1)
test_pop.append(2)

print("\n*****testing pop*****\n")
print("before pop: ", test_pop)
print("the popped item",test_pop.pop().value)
print("popped the last dll item\nnew dll: ", test_pop)
print("\n*****testing pop on one element*****\n")
print("the popped item",test_pop.pop().value)
print("popped a one element dll\nnew dll: ", test_pop)
print("\n*****testing pop on empty dll*****\n")
print("the popped item",test_pop.pop())

# ==========================
#
# Testing preprend
#
# ==========================
test_prepend = DoublyLinkedList()
for i in [2, 3]:
    test_prepend.append(i)

print("\n=============\ntesting prepend\n=============\n")
print("before prepend: ", test_prepend)
test_prepend.prepend(1)
print("after prepend: ", test_prepend)

# ==========================
#
# Testing pop first
#
# ==========================

print("\n=============\ntesting pop_first\n=============\n")
test_pop_first = DoublyLinkedList()
test_pop_first.append(2)
test_pop_first.append(1)

print("before pop first: ", test_pop_first)
print("the popped item",test_pop_first.pop_first().value)
print("after popping the first element", test_pop_first)
print("\n*******pop first with one element*******\n")
print("the popped item",test_pop_first.pop_first().value)
print("after popping the only element", test_pop_first)
print("\n*******pop first with empty dll*******\n")
print(test_pop_first.pop_first())



# ==========================
#
# Testing get first
#
# ==========================

# print("\n=============\ntesting get\n=============\n")


