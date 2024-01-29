#!/usr/bin/python3
""" define class rectangle"""


class Rectangle():
    """ inside class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the Rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""

        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if (not self.__height or not self.__width):
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self) -> str:
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if (not self.__height or not self.__width):
            return ""
        rectn = ""
        for i in range(self.__height):
            rectn += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rectn += "\n"
        return rectn

    def __repr__(self) -> str:
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
