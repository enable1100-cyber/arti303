"""Utilities for cleaning text."""


def clean_name(raw):
    """Clean a name by removing extra whitespace and using title case."""
    return " ".join(raw.split()).title()
