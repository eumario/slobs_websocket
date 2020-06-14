import functools
converters = {}

def converter(event):
    if isinstance(event,str):
        event = [event]
    
    def decorator_converter(func):
        global converters
        @functools.wraps(func)
        def wrapper_converter(*args, **kwargs):
            for ev in event:
                converters[ev] = func
        for ev in event:
            converters[ev] = func
        return wrapper_converter
    return decorator_converter

def has_converter(event):
    global converters
    return event in converters

def convert(event, data):
    global converters
    return converters[event](data)

__all__ = ["converter","has_converter","convert"]