# =========================
# Polygon Area Calculator
# =========================
# This module defines a Rectangle base class and a Square subclass.
#
# Rectangle handles all geometry for width/height shapes:
#   - Stores width and height, settable after creation
#   - Computes area, perimeter, and diagonal
#   - Draws an ASCII picture of the shape using * characters
#   - Calculates how many times another shape fits inside it
#
# Square inherits all Rectangle methods but enforces equal sides:
#   - Constructed with a single side length
#   - Overrides set_width and set_height to keep width and height in sync
#   - Adds set_side as a dedicated way to update the side length

class Rectangle:
    """ Base class representing a rectangle with independent width and height. """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        # Update width independently
        self.width = width

    def set_height(self, height):
        # Update height independently
        self.height = height

    def __str__(selff):
        # Controls what print() and str() show for a Rectangle instance
        return f"Rectangle(width={self.width}, height={self.height}"
