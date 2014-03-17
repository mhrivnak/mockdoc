mockdoc
=======

This provides a patch decorator that is a drop-in replacement for mock.patch.
All arguments are passed through to mock.patch, but this decorator additionally
does type checking. If the mocked callable has a doc block that specifies types
for any of the arguments, this decorator will ensure that all calls to that
mocked callable pass in the correct types.

Example
-------

Consider that foo and bar are somewhere on your python path.

::

    def foo():
        return bar (1, '2')

    def bar(x, y):
        """
        :type x:    int
        :type y:    int

        :rtype:     int
        """
        return x + y

And you write some tests for foo. As is frequently the case, you don't want ot
test bar, but just that foo calls bar and returns its return value.

::

    import unittest

    import mock
    import mockdoc


    class TestFoo(unittest.TestCase):
        @mock.patch('path.to.bar')
        def test_1(self, mock_bar):
            ret = foo()
            self.assertEqual(ret, mock_bar.return_value)

        @mockdoc.patch('path.to.foo')
        def test_2(self, mock_foo):
            ret = foo()
            self.assertEqual(ret, mock_bar.return_value)

The first test would miss the fact that foo called bar with the wrong type!
