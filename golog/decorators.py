"""
golog decorators
----------------
This script contains
some useful decorators

Date: 2019-01-29

Author: Lorenzo Coacci
"""
# + + + + + Libraries + + + + +
import functools
import time
import warnings
# + + + + + Libraries + + + + +

# + + + + + Decorators + + + + +
# {'status': Tru/False, 'error': ''/'Your Error',
# 'value': None/the returned value}
def sev(func):
    # outer function
    @functools.wraps(func)
    def f(*args, **kwargs):
        try:
            # inner function
            output = func(*args, **kwargs)
            try:
                if 'status' in output.keys() and 'error' in output.keys() and 'value' in output.keys():
                    result = {"status": output['status'], "error": output['error'], "value": output['value']}
                elif 'status' in output.keys() and 'error' in output.keys() and ('value' not in output.keys()):
                    result = {"status": output['status'], "error": output['error'], "value": None}
                else:
                    result = {"status": True, "error": "", "value": output}
            except Exception as e:
                try:
                    if 'status' in output.keys() and 'error' in output.keys() and ('value' not in output.keys()):
                        result = {"status": True, "error": "", "value": None}
                    else:
                        result = {"status": True, "error": "", "value": output}
                except Exception as e:
                    result = {"status": True, "error": "", "value": output}
        except Exception as e:
            print("SEV Function {} failed".format(func.__name__),
                        num_of_new_lines=1, exception=e)
            addendum = ", EXCEPTION -> {}, TRACEBACK -> {}".format(str(e), str(traceback.format_exc()))
            result = {"status": False, "error": "Reliable Function failed" + addendum, "value": None}
        return result
    return f


# {'status': Tru/False, 'error': ''/'Your Error'}
def se(func):
    # outer function
    @functools.wraps(func)
    def f(*args, **kwargs):
        try:
            # inner function
            output = func(*args, **kwargs)
            try:
                if 'status' in output.keys() and 'error' in output.keys():
                    result = {"status": output['status'], "error": output['error']}
                else:
                    result = {"status": True, "error": ""}
            except Exception as e:
                result = {"status": True, "error": ""}
        except Exception as e:
            print("SE Function {} failed".format(func.__name__),
                        num_of_new_lines=1, exception=e)
            addendum = ", EXCEPTION -> {}, TRACEBACK -> {}".format(str(e), str(traceback.format_exc()))
            result = {"status": False, "error": "Reliable Function failed" + addendum}
        return result
    return f


# try except wrapper for return func
def nocrash_return(func):
    @functools.wraps(func)
    def f(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("No Crash (Return) Function {} failed".format(func.__name__),
                        num_of_new_lines=1, exception=e)
            result = None
        return result
    return f


# try except wrapper for void func
def nocrash_void(func):
    @functools.wraps(func)
    def f(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("No Crash (Void) Function {} failed".format(func.__name__),
                        num_of_new_lines=1, exception=e)
    return f


# depracated
def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func


# to measure function performance
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
# + + + + + Decorators + + + + +

