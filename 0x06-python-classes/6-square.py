#!/usr/bin/python3

"""
File: 6-square.py
Desc: This module contains a single class defination called Size.

"""


class Square():
    """
    This square class contains some attribute definations, and method
    definations.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This method retrives the value of attribute size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        This method sets the value of the attribute size.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        This method retrives the value of the attribute position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the value of the attribute position.
        """
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(v, int) for v in value) and
                all(v >= 0 for v in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        This method computes and returns the square based on the size.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        This method prints the square with the character '#' based on the size.
        """
        if self.__size == 0:
            print("")
        else:
            for s in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print("")
