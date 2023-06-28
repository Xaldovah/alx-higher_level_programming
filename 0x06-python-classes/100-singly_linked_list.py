#!/usr/bin/python3

"""Node class represents a node of a singly linked list."""


class Node:
    """Initialize a new Node instance.

    Args:
        data (int): The data value of the node.
        n_node (Node, optional): The next node in the
        linked list. Defaults to None.

    Raises:
        TypeError: If the data is not an integer.
        TypeError: If the n_node is not None or a Node object.
    """
    def __init__(self, data, n_node=None):
        self._data = data
        self._n_node = n_node

    """Returns:
        int: The data value of the node.
    """

    @property
    def data(self):
        """Retrieve the data value of the node."""
        return self._data

    """
    Args:
        value (int): The new data value of the node.

    Raises:
        TypeError: If the value is not an integer.
    """

    @data.setter
    def data(self, value):
        """Set the data value of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    """
    Returns:
        Node: The next node in the linked list.
    """

    @property
    def n_node(self):
        """Retrieve the next node in the linked list."""
        return self._n_node

    """
    Args:
        value (Node): The new next node in the linked list.

    Raises:
        TypeError: If the value is not None or a Node object.
    """

    @n_node.setter
    def n_node(self, value):
        """Set the next node in the linked list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._n_node = value


"""SinglyLinkedList class represents a singly linked list."""


class SinglyLinkedList:
    """__init__ Initialize a new SinglyLinkedList instance.
    """
    def __init__(self):
        self.head = None

    """
    Args:
        value (int): The value to insert into the linked list.
    """

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.n_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.n_node is not None and current.n_node.data < value:
                current = current.n_node
            new_node.n_node = current.n_node
            current.n_node = new_node

    """
    Returns:
        str: The string representation of the linked list.
    """

    def __str__(self):
        """Return a string representation of the linked list."""
        output = ""
        current = self.head
        while current:
            output += str(current.data) + "\n"
            current = current.n_node
        return output.strip()
