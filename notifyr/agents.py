def observer(update_function):

    update_function = 'args[0].' + update_function + '(*args[1:], **kwargs)' # Object.update_function(Object, args)

    def class_decorator(cls):
        def update(*args, **kwargs):
            eval(update_function)

        def wrapper(cls):
            setattr(cls, 'update', update)
            return cls

        return wrapper(cls)

    return class_decorator

def observed(cls):
    def notify(*args, **kwargs):
        try:
            for each in args[0].observers:
                each.update(*args[1:], **kwargs)
        except AttributeError:
            args[0].observers = []

    def attach(cls_obj, to_attach):
        try:
            cls_obj.observers
        except AttributeError:
            cls_obj.observers = []

        cls_obj.observers.append(to_attach)


    def wrapper(cls):
        setattr(cls, 'notify', notify)
        setattr(cls, 'attach', attach)
        return cls

    return wrapper(cls)