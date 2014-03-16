import mockdoc
import mock

def bar(x, y):
    """
    :type x:    int
    :type y:    int
    """
    print x, y


@mockdoc.patch('__main__.bar', autospec=True)
def stuff(mock_bar):
    bar(1, 2)
    mock_bar.assert_called_once_with(1, 2)


stuff()
