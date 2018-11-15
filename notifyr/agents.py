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