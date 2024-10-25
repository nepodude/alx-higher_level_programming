#!/usr/bin/python3
"""Defines a rebel integer class MyInt that inverts == and != operators."""


class MyInt(int):
    """A class that inherits from int, but inverts == and != operators."""

    def __eq__(self, other):
        """Override the == operator to act as !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to act as ==."""
        return super().__eq__(other)
