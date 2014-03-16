import inspect
import re

import mock


arg_pattern = re.compile('^:type\s+(\w+):\s+([^\s]+)$')
return_pattern = re.compile('^:rtype:\s+([^\s]+)$')


def patch(*args, **kwargs):
    def _dec(f):
        patcher = mock.patch(*args, **kwargs)
        with patcher:
            original = patcher.temp_original

        docblock = inspect.getdoc(original)
        
        def replacement(mock_something, *args, **kwargs):
            ret = f(mock_something, *args, **kwargs)
            validate_calls(original, docblock, mock_something.call_args_list)
            return ret
            
        mock_obj = mock.patch(*args, **kwargs)(replacement)
        return mock_obj

    return _dec


def validate_calls(orig_func, docblock, calls):
    for call in calls:
        args = call[0]
        kwargs = call[1]
        arg_map = inspect.getcallargs(orig_func, *args, **kwargs)
        for line in docblock.split('\n'):
            match = arg_pattern.match(line)
            if match:
                name, expected_type_name = match.groups()
                expected_type = get_type(expected_type_name, orig_func)
                if expected_type is None:
                    raise ValueError('documented type [%s] could not be found' % expected_type_name)
                if not isinstance(arg_map[name], expected_type):
                    raise TypeError('mock called with wrong type for arg [%s]' % name)


def get_type(name, orig_func):
    if name in __builtins__:
        builtin = __builtins__[name]
        if isinstance(builtin, type):
            return builtin

    return mock._importer(name)

