class MyClass(object):
    pass


def bar_int(x, y):
    """
    Function that takes ints.

    :type x:    int
    :type y:    int

    :rtype:     tuple
    """
    return tuple()


def bar_full_path(x):
    """
    Function that takes a MagicMock

    :type x:    mock.MagicMock
    """
    pass


def bar_relative_path(x):
    """
    Function that takes a custom class

    :type x:    MyClass
    """
    pass


def bar_invalid_type(x):
    """
    Function that takes a custom class

    :type x:    IDontExist
    """
    pass


def bar_default_value(x='foo'):
    """
    Function that takes a custom class

    :type x:    str
    """
    pass

