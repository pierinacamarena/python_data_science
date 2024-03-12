def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items
    of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """

    if function:
        # generator expressions
        return (item for item in iterable if function(item))
    # filter falsy values (0, False, None, etc)
    return (item for item in iterable if item)
