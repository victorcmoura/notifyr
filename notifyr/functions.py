def target(func):
    def decorated_func(*args, **kwargs):
        result = func(*args, **kwargs)
        args[0].notify(*args, **kwargs)
        return result
    return decorated_func