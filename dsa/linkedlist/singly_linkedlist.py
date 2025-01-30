class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}->"


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __str__(self):
        out = ""
        temp = self.head
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return True

    set_head = prepend

    def pop_first(self):
        temp = self.head

        if not temp:
            # empty list
            return

        self.head = temp.next
        temp.next = None

        if self.head is None:
            # list contained only one item
            self.tail = self.head

        self.length -= 1

        return temp

    def pop(self):
        temp = self.head

        count = 1
        while temp is not None:
            if count == 1 and temp.next is None:
                # list contained one item
                self.tail = None
                self.head = None
            elif temp.next is not None and temp.next.next is None:
                self.tail = temp
                temp = temp.next
                self.tail.next = None
            else:
                count += 1
                temp = temp.next
                continue
            self.length -= 1
            return temp

    def remove(self, index):
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        before = self.get(index - 1)
        if before is None:
            return

        temp = before.next
        if temp is None:
            # the index may have been bigger than the length of the linkedlist
            return

        before.next = temp.next
        temp.next = None

        self.length -= 1
        return temp

    # def set_value(self, index, value):
    #     if index < 0:
    #         return False
    #
    #     before = self.get(index - 1)
    #
    #     if before is None:
    #         return False
    #
    #     node = Node(value)
    #
    #     temp = before.next
    #     if temp is not None:
    #         node.next = temp.next
    #         temp.next = None
    #
    #     before.next = node
    #
    #     self.length += 1
    #
    #     return True

    def set(self, index, value):
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        before = self.get(index - 1)

        if before is None:
            # applicable when index is out of range i.e.
            # below ZERO or above the length of the list
            return False

        node = Node(value)
        node.next = before.next
        before.next = node

        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index > self.length - 1:
            # 2nd condition is not necessary, but an optimal step for avoiding unnecessary loop
            return

        temp = self.head

        i = 0
        while temp is not None:
            if i == index:
                return temp

            temp = temp.next
            i += 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        # for _ in range(self.length):
        #     after = temp.next
        #     temp.next = before
        #     before = temp
        #     temp = after

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        if self.tail is not None:
            self.tail.next = None

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next
