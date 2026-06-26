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

    def __str__(self):
        # Controls what print() and str() show for a Rectangle instance
        return f"Rectangle(width={self.width}, height={self.height}"

    def get_area(self):
        # Area formula
        return self.width * self.height

    def get_perimeter(self):
        # Perimeter formula
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Diagonal via Pythagoras
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Dimensions over 50 can't be drawn
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Build one row of stars and repeat it height times
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        # Integer division tells how many times the shape fits along each axis
        # Multiply both axes for the total count (no rotations allowed)
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    """Rectangle subclass that enforces equal width and height at all times."""

    def __init__(self, side):
        # Pass the same value for both width and height to the parent
        super().__init__(side, side)

    def __str__(self):
        # Overrides Rectangle's __str__ — width and height are always equal
        # so we only need to show one value labelled as "side"
        return f"Square(side={self.width})"