class Fraction:
    """Represents a mathematical fraction."""

    def __init__(self, numerator, denominator):
        """Initializes a Fraction object.

        Args:
          numerator: The numerator of the fraction (int).
          denominator: The denominator of the fraction (int, cannot be 0).

        Raises:
          ZeroDivisionError: If denominator is 0.
        """
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Returns a string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"

    def get_numerator(self):
        """Returns the numerator of the fraction."""
        return self.numerator

    def set_numerator(self, numerator):
        """Sets the numerator of the fraction."""
        self.numerator = numerator

    def get_denominator(self):
        """Returns the denominator of the fraction."""
        return self.denominator

    def set_denominator(self, denominator):
        """Sets the denominator of the fraction, checking for division by zero.

        Args:
          denominator: The new denominator (int, cannot be 0).

        Raises:
          ZeroDivisionError: If denominator is 0.
        """
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self.denominator = denominator

    def simplify(self):
        """Simplifies the fraction by finding the greatest common divisor (GCD) of numerator and denominator and dividing both by the GCD."""
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def _gcd(self, a, b):
        """Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def add(self, other):
        """Adds two fractions."""
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator).simplify()
        else:
            raise TypeError("Can only add Fraction objects")

    def subtract(self, other):
        """Subtracts two fractions."""
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator).simplify()
        else:
            raise TypeError("Can only subtract Fraction objects")

    def multiply(self, other):
        """Multiplies two fractions."""
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator).simplify()
        else:
            raise TypeError("Can only multiply Fraction objects")

    def divide(self, other):
        """Divides two fractions."""
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator).simplify()
        else:
            raise TypeError("Can only divide by Fraction objects")

    def is_equal(self, other):
        """Checks if two fractions are equal."""
        if isinstance(other, Fraction):
            self.simplify()
            other.simplify()
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            return False
