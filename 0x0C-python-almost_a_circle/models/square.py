#!/usr/bin/python3
"""import Rectangle class module"""
from models.rectangle import Rectangle
"""Square class module"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
