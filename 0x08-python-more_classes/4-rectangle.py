#!/usr/bin/python3

"""
File: 4-rectangle.py
Desc: This file contains a single class defination called Rectangle

"""


class Rectangle():
    """
    This is a class defination called Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method retrives the value of attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the value of the attribute height.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        This method retrives the value of attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the value of the attribute height.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        This method computes the area of rectangle based on the
        height and width value.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method computes the permeter of rectangle based on
        the height and width value.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Nicely printable string representation of an object of class
        rectangle.
        """
        ret_val = ""
        if (self.__height == 0 or self.__width == 0):
            return ret_val
        for i in range(self.__height):
            [print("#", end="") for ch in range(self.__width)]
            if i < self.__height - 1:
                print("")
        return ret_val

    def __repr__(self):
        """
        An instance method that returns an official string representation
        of an instance.
        """
        ret_val = f'Rectangle({self.__width}, {self.__height})'
        return ret_val
