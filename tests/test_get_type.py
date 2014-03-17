import os
import sys
import unittest

from mock import Mock, MagicMock

import mockdoc

# testing code that we need on the python path but don't want to be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../test_data/'))
import bar


class TestPatch(unittest.TestCase):
    def test_full_python_path(self):
        @mockdoc.patch('bar.bar_full_path', autospec=True)
        def stuff(mock_bar):
            c = MagicMock()
            bar.bar_full_path(c)
            mock_bar.assert_called_once_with(c)

        stuff()

    def test_incorrect_full_python_path(self):
        @mockdoc.patch('bar.bar_full_path', autospec=True)
        def stuff(mock_bar):
            c = Mock()
            bar.bar_full_path(c)

        # passes Mock() instead of MagicMock()
        self.assertRaises(TypeError, stuff)

    def test_builtin_type(self):
        @mockdoc.patch('bar.bar_int', autospec=True)
        def stuff(mock_bar):
            c = MagicMock()
            bar.bar_int(1, 2)
            mock_bar.assert_called_once_with(1, 2)

        stuff()

    def test_incorrect_builtin_type(self):
        @mockdoc.patch('bar.bar_int', autospec=True)
        def stuff(mock_bar):
            c = MagicMock()
            bar.bar_full_path(1, 'word')

        # passes a string instead of an int
        self.assertRaises(TypeError, stuff)

    def test_relative_path(self):
        @mockdoc.patch('bar.bar_relative_path', autospec=True)
        def stuff(mock_bar):
            c = bar.MyClass()
            bar.bar_relative_path(c)
            mock_bar.assert_called_once_with(c)

        stuff()

    def test_incorrect_relative_path(self):
        @mockdoc.patch('bar.bar_relative_path', autospec=True)
        def stuff(mock_bar):
            c = bar.MyClass()
            bar.bar_relative_path('word')

        # passes a string instead of a MyClass
        self.assertRaises(TypeError, stuff)

    def test_keyword(self):
        """pass one of the arguments as a keyword"""
        @mockdoc.patch('bar.bar_int', autospec=True)
        def stuff(mock_bar):
            c = MagicMock()
            bar.bar_int(1, y=2)
            mock_bar.assert_called_once_with(1, y=2)

        stuff()

    def test_invalid_type(self):
        @mockdoc.patch('bar.bar_invalid_type', autospec=True)
        def stuff(mock_bar):
            bar.bar_invalid_type('word')

        # documents a type that doesn't exist
        self.assertRaises(ValueError, stuff)

    def test_default_value(self):
        @mockdoc.patch('bar.bar_default_value', autospec=True)
        def stuff(mock_bar):
            bar.bar_default_value()

        stuff()


class TestGetType(unittest.TestCase):
    def test_int(self):
        ret = mockdoc.get_type('int', lambda x: None)

        self.assertTrue(ret is int)

    def test_str(self):
        ret = mockdoc.get_type('str', lambda x: None)

        self.assertTrue(ret is str)

    def test_basestring(self):
        ret = mockdoc.get_type('basestring', lambda x: None)

        self.assertTrue(ret is basestring)

    def test_list(self):
        ret = mockdoc.get_type('list', lambda x: None)

        self.assertTrue(ret is list)
