#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevents dynamic creation of attributes except first_name."""

    __slots__ = ["first_name"]
