from math import sqrt, cos, sin, atan


class Vector:
    """Class for methods that have been factored out from Rectangluar and Polar Vectors"""

    def __init__(self, *args):
        """Users should specify rectangular or polar instead"""
        raise NotImplementedError("Specify RectangularVector or PolarVector.")

    # Define "getters" for x, y, mag, and angle
    def get_x(self):
        """Returns x-component of vector."""
        return self._x

    def get_y(self):
        """Returns y-component of vector."""
        return self._y

    def get_mag(self):
        """Returns magnitude of vector."""
        return self._mag

    def get_ang(self):
        """Returns angle of vector."""
        return self._ang

    # Define methods for eq, add, rectangular, polar, and dot
    def rectangular(self):
        """Return a RectangularVector with the same components."""
        return RectangularVector(self._x, self._y)

    def polar(self):
        """Return a PolarVector with the same components."""
        return PolarVector(self._mag, self._ang)

    def __eq__(self, other):
        """Check if two vectors are equal using the x and y components. to 3 decimal places."""
        return round(self._x, 3) == round(other.get_x(), 3) and round(self._y, 3) == round(other.get_y(), 3)

    def __add__(self, other):
        """Add two vectors together and return a new vector."""
        return RectangularVector(self._x + other.get_x(), self._y + other.get_y())

    def dot(self, other):
        """Return the dot product of two vectors."""
        return self._x * other.get_x() + self._y * other.get_y()

    def __mul__(self, *args):
        """Raises a NotImplementedError. Use the dot method instead, cross product is not defined."""
        raise NotImplementedError("Use the dot method instead. Cross product is not yet supported.")


class RectangularVector(Vector):
    """Rectangular vectors have an x and y component."""

    def __init__(self, x, y):
        """Creates a new vector with given x- and y- attributes."""
        self._x = x
        self._y = y
        self._update()  # add self._mag and self._ang

    def _update(self):
        """Update the magnitude and angle of the vector."""
        self._mag = sqrt(self._x ** 2 + self._y ** 2)
        self._ang = atan(self._y / self._x)

    # Define public setters for x and y
    def set_x(self, x):
        """Set the x-component of the vector."""
        self._x = x
        self._update()

    def set_y(self, y):
        """Set the y-component of the vector."""
        self._y = y
        self._update()

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"RectangularVector({self._x}, {self._y})"


class PolarVector(Vector):
    """Polar vectors have a magnitude and angle."""

    def __init__(self, mag, ang):
        """Creates a new vector with given magnitude and angle attributes."""
        self._mag = mag
        self._ang = ang
        self._update()  # add self._x and self._y

    def _update(self):
        """Update the x and y components of the vector."""
        self._x = self._mag * cos(self._ang)
        self._y = self._mag * sin(self._ang)

    # Define public setters for mag and ang
    def set_mag(self, mag):
        """Set the magnitude of the vector."""
        self._mag = mag
        self._update()

    def set_ang(self, ang):
        """Set the angle of the vector."""
        self._ang = ang
        self._update()

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"PolarVector({self._mag}, {self._ang})"
