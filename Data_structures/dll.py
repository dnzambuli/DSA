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

    def get(self, index) -> Node:
        """
        get the node at a given index
        :param index:
        :return:
        """
        # edge case: index is less than 0 or geq size of dll

        temp = self.head
        if index > self.size /2:
            for _ in range(index):
                temp = temp.next
        # edge case: the value is found in an index gt the center
        else:
            temp = self.tail
            for _ in range(self.size -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value) -> bool:
        """
            set the value at a given index to be value
            :param index:
            :param value:
            :return:
            """
        target = self.get(index)
        if target is not None:
            target.value = value
            return True
        return False

    def insert_value(self, index, value) -> bool:
        """
            insert a value at a particulat index
            :param index:
            :param value:
            :return:
            """
        # edge case: index is negative index is greater than the size
        if index < 0 or index > self.size:
            return False

        # edge case: insert at the beginning
        if index == 0:
            self.prepend(value)

        # edge case: insert at the end
        if index == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            prev = self.get(index -1)
            after = prev.next
            new_node.prev = prev
            new_node.next = after
            prev.next = new_node
            after.prev = new_node
        self.size += 1
        return True

    def remove(self, index) -> Node:
        """
            remove Node at index and return the removed node
            :param index:
            :return Node:
            """
        # edge case: index is less than 0 or geq size of dll
        if index < 0 or index >= self.size:
            return None

        # edge case: remove from start
        if index == 0:
            self.pop_first()

        # edge case: remove from the end
        if index == self.size - 1:
            self.pop()

        target = self.get(index)
        target.next.prev = target.prev
        target.prev.next = target.next
        target.next = None
        target.prev = None

        self.size -= 1
        return target



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
# Testing get
#
# ==========================

print("\n=============\ntesting get\n=============\n")

test_get = DoublyLinkedList()
sample_data = [0, 1, 2, 3]
for i in sample_data:
    test_get.append(i)

print("content of the dll: ", test_get)
print("\nget the value at index 1\n")
print(test_get.get(1).value)
print("\nget the value at index 2\n")
print(test_get.get(2).value)


# ==========================
#
# Testing set
#
# ==========================

print("\n=============\ntesting set\n=============\n")

test_set = DoublyLinkedList()
sample_data = [0, 1, 2, 3]
for i in sample_data:
    test_set.append(i)

print("content of the dll: ", test_set)
print("\nset the value at index 1 to be 22\n")
test_set.set_value(1, 22)
print("content of the dll: ", test_set)


# ==========================
#
# Testing insert at index
#
# ==========================

print("\n=============\ntesting insert at index\n=============\n")

test_insertAt = DoublyLinkedList()
sample_data = [0, 1, 2, 3]
for i in sample_data:
    test_insertAt.append(i)

print("content of the dll: ", test_insertAt)
print("\nInsert 22 at index 2\n")
test_insertAt.insert_value(2, 22)
print("content of the dll: ", test_insertAt)

# ==========================
#
# Testing remove at index
#
# ==========================

print("\n=============\ntesting remove at index\n=============\n")

test_remove = DoublyLinkedList()
sample_data = [0, 1, 2, 3]
for i in sample_data:
    test_remove.append(i)

print("content of the dll: ", test_remove)
print("\nRemove value at index 2\n")
test_remove.remove(2)
print("content of the dll: ", test_remove)
