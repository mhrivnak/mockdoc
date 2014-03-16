import re

import mock

def patch(*args, **kwargs):

    def _dec(f):
        patcher = mock.patch(*args, **kwargs)
        with patcher:
            docblock = patcher.temp_original.__doc__
        
        def foo(mock_something, *args, **kwargs):
            ret = f(mock_something, *args, **kwargs)
            validate_calls(docblock, mock_something.call_args)
            return ret
            
        mock_obj = mock.patch(*args, **kwargs)(foo)
        return mock_obj

    return _dec

def validate_calls(docblock, calls):
    print docblock
    print calls
