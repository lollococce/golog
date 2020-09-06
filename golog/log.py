"""
golog log
---------
This script contains
basic functions for logging

Date: 2019-01-29

Author: Lorenzo Coacci
"""
# + + + + + Libraries + + + + +
# to manage os
import os
# import decoratos
from .decorators import *
# to manage datetime, date, timedelta
from datetime import datetime, date, timedelta, timezone
# to manage traceback
import traceback
# - - optional packages - -
try:
    # to manage jsons
    import json
    # to manage colored text
    from termcolor import colored as col
    # to hide passwords
    import getpass
    # to count occurences
    from collections import Counter
    # to create progress bars
    from progressbar import progressbar
    # to manage validators
    import validators
except ImportError as exc:
    print(
        "Couldn't import some packages for logging." \
        "Are you sure everything is installed and " \
        "available on your PYTHONPATH environment variable? Did you " \
        f"forget to activate a virtual environment? -> {str(exc)}"
    )
# + + + + + Libraries + + + + +


# + + + + + Settings + + + + +
HOME = os.path.expanduser("~")

# - - Colors - -
RED = 'red'
YELLOW = 'yellow'
WHITE = 'white'
GREEN = 'green'
GREY = 'grey'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
TITLE_COLOR = MAGENTA
DEBUG_COLOR = BLUE
INFO_COLOR = WHITE
WARNING_COLOR = YELLOW
ERROR_COLOR = RED
SUCCESS_COLOR = GREEN
# - - Colors - -
# + + + + + Settings + + + + +


# + + + + + Functions + + + + +
@nocrash_return
def label_format(
    msg, num_of_new_lines=0, num_of_tabs=0,
    label="LABEL: ", timestamp=True,
    exception=None
):
    """RETURN : Return a string formatted in a LABEL way"""
    # number of new lines before text
    if timestamp:
        label = '[' + str(datetime.now()) + '] ' + label

    if num_of_new_lines > 0:
        for _ in range(num_of_new_lines):
            print("\n")
    if num_of_tabs > 0:
        for _ in range(num_of_tabs):
            print("\t")
    # print labeled message
    msg = str(msg)
    # traceback?
    if exception is not None:
        msg += ", EXCEPTION -> {}, TRACEBACK -> {}".format(str(exception), str(traceback.format_exc()))
    # return
    if msg is None:
        return None
    else:
        return label + msg


@se
def label_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=None, label="LABEL: ", timestamp=True,
    exception=None
):
    """VOID : Print out a labeled message with a nice format"""
    # number of new lines before text
    if timestamp:
        label = '[' + str(datetime.now()) + '] ' + label

    if num_of_new_lines > 0:
        for _ in range(num_of_new_lines):
            print("\n")
    if num_of_tabs > 0:
        for _ in range(num_of_tabs):
            print("\t")
    # print labeled message
    msg = str(msg)
    # traceback?
    if exception is not None:
        msg += ", EXCEPTION -> {}, TRACEBACK -> {}".format(str(exception), str(traceback.format_exc()))
    if color is None:
        if msg is None:
            print(None)
        else:
            print(label + msg)
    else:
        try:
            if msg is None:
                print(None)
            else:
                print(col(label + msg, color))
        except Exception as e:
            if msg is None:
                print(None)
            else:
                print(label + msg)


@se
def output_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=INFO_COLOR, output_label=" >> ",
    timestamp=True, exception=None
):
    """VOID : Print out an output message with a nice format"""
    # output print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=output_label, timestamp=timestamp,
                exception=exception)


@se
def error_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=ERROR_COLOR, error_label="* * * ERROR * * * : ",
    timestamp=True, exception=None
):
    """VOID : Print out an error message with a nice format"""
    # error print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=error_label, timestamp=timestamp,
                exception=exception)


@se
def warning_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=WARNING_COLOR, warning_label="* WARNING * : ",
    timestamp=True, exception=None
):
    """VOID : Print out a warning message with a nice format"""
    # warning print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=warning_label, timestamp=timestamp,
                exception=exception)


@se
def info_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=INFO_COLOR, info_label="INFO : ",
    timestamp=True, exception=None
):
    """VOID : Print out an info message with a nice format"""
    # info print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=info_label, timestamp=timestamp,
                exception=exception)


@se
def success_print(
    msg, num_of_new_lines=0, num_of_tabs=0,
    color=SUCCESS_COLOR, success_label="SUCCESS : ",
    timestamp=True, exception=None
):
    """VOID : Print out a success message with a nice format"""
    # success print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=success_label, timestamp=timestamp,
                exception=exception)


@nocrash_return
def error_format(
    msg, num_of_new_lines=0, num_of_tabs=0,
    label="* * * ERROR * * *: ", timestamp=True,
    exception=None
):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


@nocrash_return
def warning_format(
    msg, num_of_new_lines=0, num_of_tabs=0,
    label="* WARNING *: ", timestamp=True,
    exception=None
):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


@nocrash_return
def success_format(
    msg, num_of_new_lines=0, num_of_tabs=0,
    label="SUCCESS: ", timestamp=True,
    exception=None
):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


def list_format(
    list_to_format,
    intro_label="Printing the list:",
    color=WHITE, show_debug=True
):
    """RETURN : Format a list with a nice format"""
    # dict print
    try:
        list_str = label_format('\n' + intro_label + ' [length : {}]'.format(len(list_to_format)) + '\n', label="")
        for element in list_to_format:
            list_str += "  - {}\n".format(element)
        return list_str
    except Exception as e:
        if show_debug:
            warning_print("Cannot get list in nice format, printing standard", exception=e)
        return list_to_format


def dict_format(
    dict_to_format, intro_label="Printing the dict:",
    color=WHITE, show_debug=True
):
    """RETURN : Format a dict of keys and values with a nice format"""
    # dict print
    try:
        dict_str = label_format('\n' + intro_label + '\n', label="")
        for key, value in dict_to_format.items():
            dict_str += "  - {} : {}\n".format(str(key), str(value))
        return dict_str
    except Exception as e:
        if show_debug:
            warning_print("Cannot get dict in nice format, printing standard", exception=e)
        return dict_to_format


@se
def list_print(
    list_to_print, intro_label="Printing the list:",
    color=WHITE, show_length=True, show_debug=True
):
    """VOID : Print out a list of values with a nice format"""
    # list print
    try:
        if show_length:
            label_print('\n' + intro_label + ' [length : {}]'.format(len(list_to_print)) + '\n', label="", color=color)
        else:
            label_print('\n' + intro_label + '\n', label="", color=color)
        for element in list_to_print:
            print("  - {}".format(element))
        new_line()
    except Exception as e:
        if show_debug:
            warning_print("Cannot print list in nice format, printing standard", exception=e)
        print(list_to_print)


@se
def dict_print(
    dict_to_print, intro_label="Printing the dict:",
    color=WHITE, show_debug=True
):
    """VOID : Print out a dict of keys and values with a nice format"""
    # dict print
    try:
        label_print('\n' + intro_label + '\n', label="", color=color)
        for key, value in dict_to_print.items():
            print("  - {} : {}".format(str(key), str(value)))
        new_line()
    except Exception as e:
        if show_debug:
            warning_print("Cannot print dict in nice format, printing standard", exception=e)
        print(dict_to_print)


@se
def print_color(msg, color, show_debug=True):
    """VOID : print a text with 'print' but colored"""
    try:
        print(col(str(msg), color))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def print_magenta(msg, show_debug=True):
    """VOID : print a text with 'print' but colored magenta"""
    try:
        print(col(str(msg), color=MAGENTA))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def print_blue(msg, show_debug=True):
    """VOID : print a text with 'print' but colored blue"""
    try:
        print(col(str(msg), color=BLUE))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def print_red(msg, show_debug=True):
    """VOID : print a text with 'print' but colored red"""
    try:
        print(col(str(msg), color=RED))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def print_yellow(msg, show_debug=True):
    """VOID : print a text with 'print' but colored yellow"""
    try:
        print(col(str(msg), color=YELLOW))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def print_green(msg, show_debug=True):
    """VOID : print a text with 'print' but colored green"""
    try:
        print(col(str(msg), color=GREEN))
    except Exception as e:
        if show_debug:
            warning_print("Probably cannot recognize color", exception=e)
        print(str(msg))


@se
def welcome(color=WHITE, num_of_new_lines=0, num_of_tabs=0):
    """VOID : Print out a welcome message with a nice format"""
    # number of new lines before text
    if num_of_new_lines > 0:
        for _ in range(num_of_new_lines):
            print("\n")
    if num_of_tabs > 0:
        for _ in range(num_of_tabs):
            print("\t")
    # print welcome message
    if color is None:
        print("\n\n* * * * * * * * * * * * * * * * * *")
        print("*            WELCOME              *")
        print("* * * * * * * * * * * * * * * * * *\n")
    else:
        try:
            print(col("\n\n* * * * * * * * * * * * * * * * * *", color))
            print(col("*            WELCOME              *", color))
            print(col("* * * * * * * * * * * * * * * * * *\n", color))
        except Exception:
            print("\n\n* * * * * * * * * * * * * * * * * *")
            print("*            WELCOME              *")
            print("* * * * * * * * * * * * * * * * * *\n")


@se
def new_line():
    """VOID : Print out new line"""
    print('\n')


@se
def new_lines(n):
    """VOID : Print out n new lines"""
    for _ in range(n):
        new_line()
# + + + + + PRINT + + + + +


# + + + + + USER INPUT + + + + +
@nocrash_return
def input_color(
    msg, color, parse_none=False,
    show_debug=True
):
    """RETURN : ask a user input but with colored msg and return it"""
    try:
        user_input = input(col(msg, color))
    except Exception as e:
        user_input = input(msg)
        if show_debug:
            warning_print("Error, probably cannot recognize color", exception=e)
    if parse_none:
        if user_input.lower() == 'none':
            user_input = None
    return user_input


@nocrash_return
def ask_input_int(
    msg, to_bool=False, color=None,
    security_stop=1000, show_debug=True
):
    """
    RETURN : Ask an int to the user and return it as int (or bool)

    Parameters
    ----------
    msg : string
        An info string message for the user before the input
    to_bool (optional) : bool
        Cast the int to bool?
    color (optional) : string
        The string or const var for termcolor
        'red', 'yellow' etc or lc.RED, lc.YELLOW, etc
    security_stop (optional) : int
        If a machine gets in a loop after 1000 errors it stops
    show_debug (optional) : bool
        Show debug info?

    Returns
    -------
    input : int (or bool)
        * The user input transormed to int (or bool)
        OR
        * None, if "None" or "none" is the input
    """
    user_input = input_color(msg, color=color, show_debug=False)
    if (user_input == "None") or (user_input == "none"):
        return None
    try:
        if to_bool:
            # parse it to int and evaluate bool
            input_bool = (int(user_input) >= 1)
            return input_bool
        else:
            # parse it to int
            input_int = int(user_input)
            return input_int
    except (ValueError, TypeError) as e:
        # cannot parse it to int or bool
        if show_debug:
            error_print("Cannot cast your input", exception=e)
        # try again!
        if security_stop > 0:
            return ask_input_int(msg=msg, to_bool=to_bool,
                                 color=color, security_stop=security_stop - 1)
        else:
            return None
    except Exception as e:
        # general error
        if show_debug:
            error_print("General error while casting your input", exception=e)
        # try again!
        if security_stop > 0:
            return ask_input_int(msg=msg, to_bool=to_bool,
                                 color=color, security_stop=security_stop - 1)
        else:
            return None


@nocrash_return
def ask_input_login(
    pre_msg="", color=None,
    username_label="USERNAME",
    password_label="PASSWORD",
    pin_label=None,
    show_debug=False
):
    """RETURN : dict - ask a user the login and save it"""
    print_color("\n" + pre_msg + " LOGIN:\n", color=color, show_debug=show_debug)
    username = input_color("\t{}:  ".format(str(username_label)), color=color, show_debug=show_debug)
    try:
        password = getpass.getpass(col("\t{}:  ".format(str(password)), color))
    except Exception:
        password = getpass.getpass("\t{}:  ".format(str(password_label)))
    try:
        if pin_label is None:
            login = {"username": username, "password": password}
        else:
            pin = input_color("\t{}:  ".format(str(pin_label)), color=color, show_debug=show_debug)
            login = {"username": username, "password": password, "pin": pin}
    except Exception as e:
        if show_debug:
            error_print("Cannot save login info", exception=e)
        login = {"username": None, "password": None}
    return login
# + + + + + USER INPUT + + + + +
# + + + + + Functions + + + + +