#!/usr/bin/python3
"""Define a node and a sorted singly linked list."""


class Node:
    """Store an integer and a link to the next node."""

    def __init__(self, data, next_node=None):
        """Initialize the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the stored integer."""
        return self.__data

    @data.setter
    def data(self, value):
        """Validate and store the integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Validate and store the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Store nodes in increasing order."""

    def __init__(self):
        """Create an empty list."""
        self.__head = None

    def __str__(self):
        """Return one integer per line."""
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)

    def sorted_insert(self, value):
        """Insert a new node in increasing order."""
        node = Node(value)
        previous = None
        current = self.__head

        while current is not None and current.data <= value:
            previous = current
            current = current.next_node

        node.next_node = current
        if previous is None:
            self.__head = node
        else:
            previous.next_node = node
