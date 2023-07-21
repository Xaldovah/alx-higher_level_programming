#!/usr/bin/python3
"""import Rectangle class module"""
from models.rectangle import Rectangle
"""Square class module"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        """Display the square"""
        for _ in range(self.y):
            print()
        for _ in range(self.size):
            print(" " * self.x + "#" * self.size)

    def update(self, *args, **kwargs):
        """Update"""
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
