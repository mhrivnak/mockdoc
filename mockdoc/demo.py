import mockdoc
from mock import Mock


def bar(x, y):
    """
    :type x:    int
    :type y:    mock.Mock
    """
    print x, y


class Crap(object):
    pass

@mockdoc.patch('__main__.bar', autospec=True)
def stuff(mock_bar):
    c = Mock()
    bar(1, c)
    mock_bar.assert_called_once_with(1, c)


stuff()

