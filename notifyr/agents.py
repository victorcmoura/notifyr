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

def observed(observers_list_function):

    pre_eval_observers_list = 'args[0].' + observers_list_function + '()' # Object.observers_list_function()

    def class_decorator(cls):
        def notify(*args, **kwargs):
            for each in eval(pre_eval_observers_list):
                each.update(*args[1:], **kwargs)

        def wrapper(cls):
            setattr(cls, 'notify', notify)
            return cls

        return wrapper(cls)

    return class_decorator