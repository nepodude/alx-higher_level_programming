#!/usr/bin/python3

"""Defines a Node class and a SinglyLinkedList class."""

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node with data and next_node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node): The next node to link to.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()  # Remove the trailing newline

    def sorted_insert(self, value):
        """Inserts a new Node into the list in sorted order.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)

        # If the list is empty or the new value is less than the head
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse the list to find the correct position
        current = self.__head
        while current.next_node is not None and current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
