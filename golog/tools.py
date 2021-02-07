"""
golog tools
-----------
This script contains
basic functions
for general tools

Date: 2019-01-29

Author: Lorenzo Coacci
"""
# + + + + + Libraries + + + + +
# import decoratos
from .log import (
    warning_print,
    nocrash_return,
    sev,
    os
)
# to count occurences
from collections import Counter
# to create progress bars
from alive_progress import alive_bar
# to manage validators
import validators
# + + + + + Libraries + + + + +


# + + + + + Functions + + + + +
# + + + + + CAST + + + + +
# - - TO CAST [NO CRASH] - -
@nocrash_return
def to_int(object):
    """RETURN : None if unable to convert to int"""
    return int(object)

@nocrash_return
def to_str(object):
    """RETURN : None if unable to convert to str"""
    return str(object)

@nocrash_return
def to_list(object):
    """RETURN : None if unable to convert to list"""
    return list(object)

@nocrash_return
def to_dict(object):
    """RETURN : None if unable to convert to dict"""
    return dict(object)

@nocrash_return
def to_set(object):
    """RETURN : None if unable to convert to set"""
    return set(object)
# - - TO CAST [NO CRASH] - -

# - - VALIDATE TYPES - -
def is_int(object):
    """RETURN : True/False """
    return isinstance(object, int)

def is_str(object):
    """RETURN : True/False """
    return isinstance(object, str)

def is_list(object):
    """RETURN : True/False """
    return isinstance(object, list)

def is_dict(object):
    """RETURN : True/False """
    return isinstance(object, dict)

def is_url(object):
    """RETURN : True/False """
    if is_str(object):
        pass
    else:
        if to_str(object) is None:
            return False
        else:
            object = to_str(object)
    if validators.url(object):
        return True
    else:
        return False
# - - VALIDATE TYPES - -

# - - ENCODE/DECODE - -
@nocrash_return
def decode_length_delta(length, delta, as_str=True):
    """RETURN : A tuple (start_date, end_date) from a relative date l, d (days)"""
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=length)
    # apply delta
    end_date = end_date - timedelta(days=delta)
    start_date = start_date - timedelta(days=delta)
    if as_str:
       end_date = end_date.strftime("%Y-%m-%d")
       start_date = start_date.strftime("%Y-%m-%d")
    return (start_date, end_date)
# - - ENCODE/DECODE - -
# + + + + + CAST + + + + +

# + + + + + FORMATTING + + + + +
@nocrash_return
def json_stringify(label, value):
    if isinstance(value, int):
        label = str(label)
        return '{' + '\\' + '"' + label + '\\' + '":' + '{}'.format(value) + '}'
    else:
        value = str(value)
        label = str(label)
        return '{' + '\\' + '"' + label + '\\' + '":' + '\\' + '"{}'.format(value) + '\\' + '"}'


@nocrash_return
def dict_stringify(dict_to_prepare):
    return dict_to_prepare.replace('"', '\\"')
# + + + + + FORMATTING + + + + +


# + + + + + TOOLS + + + + +
@nocrash_return
def correct_filepath(string, slash_remove=False):
    """RETURN : The file path with '/' at the end
    if the developer/user forgot it or viceversa"""
    if slash_remove:
        new_string = str(string) + '/' if string[-1] != '/' else str(string)[:-1]
    else:
        new_string = str(string) + '/' if string[-1] != '/' else string
    return new_string


@nocrash_return
def correct_nonlist(to_assert_list):
    """RETURN : Transform any element to list if it's not a list
    if the developer/user forgot it"""
    if not isinstance(to_assert_list, list):
        to_assert_list = [to_assert_list]
    return to_assert_list


@nocrash_return
def filepath_exists(string, show_debug=True):
    """RETURN : True/False if valid file path"""
    check = os.path.exists(string)
    if not check:
        if show_debug:
            warning_print("This filepath {} is not a valid filepath".format(str(string)))
    return check


@nocrash_return
def is_anagram(s1, s2):
    """RETURN : True/False if anagram"""
    return set(s1) == set(s2)


@nocrash_return
def frequency_elements(list_input):
    """RETURN : a dict with occurences of elements"""
    c = Counter(list_input)
    return c
# + + + + + TOOLS + + + + +


# + + + + + PROCESSES/CHAINS + + + + +
@sev
def perform(function, *args, show_debug=True):
    """
    RETURN :  {"status": True/False, "error": error_msg, "value": value},
              perform a function

    Parameters
    ----------
    function : function python
        The function to perform
    *args : *args
        The args of the function
    show_debug : bool
        Show debug info?

    Returns
    -------
    result :  {"status": True/False, "error": error_msg, "value": value}
    """
    # prepare args and kwargs
    kwargs = args[0]
    args = args[1]
    if type(args) is not tuple:
        args = tuple([args])
    # execute func
    action = function(*args, **kwargs)
    # return
    return action
# + + + + + PROCESSES/CHAINS + + + + +
# + + + + + Functions + + + + +
