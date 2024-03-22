def list_check(lst):
    return all(type(l) == list for l in lst)
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
