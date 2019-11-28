def cyclic_rotation(string, number):
    """
    >>> cyclic_rotation('abcde', 2)
    'deabc'
    """
    return (string[-number:] + string[:len(string) - number])