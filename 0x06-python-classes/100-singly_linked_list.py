#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        if self.__head is None:
            node = Node(value, self.__head)
            self.__head = node
            return

        node = Node(value)
        curr = self.__head

        if (curr.data > value):
            node.next_node = self.__head
            self.__head = node
            return

        while curr.next_node is not None:
            if curr.next_node.data < value:
                curr = curr.next_node
            else:
                break

        if curr.next_node is None:
            curr.next_node = node
        else:
            next_node = curr.next_node
            curr.next_node = node
            node.next_node = next_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        curr = self.__head
        values = []
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(values)
