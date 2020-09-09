def decorator(func):
    """"""

    import csv
    import functools

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        """"""

        result = func(*args, **kwargs)
        result = csv.writer(result)
        return result

    return wrapped