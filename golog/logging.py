"""
golog logging
-------------
This script contains
basic structure funcs for pysuperbolt

Date: 2019-01-29

Author: Lorenzo Coacci
"""

# + + + + + Libraries + + + + +
# to manage os
import os
# to manage logging
import logging
# import decoratos
from .decorators import *
# to manage datetime, date, timedelta
from datetime import datetime, date, timedelta, timezone
# import everything else (that could fail)
try:
    # to manage traceback
    import traceback
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
except ImportError as e:
    raise ImportError(
        "Couldn't import some packages for logging."
        "Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from e
# + + + + + Libraries + + + + +


# + + + + + Settings + + + + +
HOME = os.path.expanduser("~")

# - - Emojii - -
EYES_UP = '🙄'
AHAH = '😂'
AHAHAH = '🤣'
SMILE = '😊'
BLINK = '😉'
ANGRY = '🤬'
MONEY_FACE = '🤑'
CRY_SUPER = '😭'
CRY = '😢'
DISGUST = '🤢'
GHOST = '👻'
CHAMPAGNE = '🍾'
SHHH = '🤫'
# -- Emoji - -

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

ON_GREY = 'on_grey'
ON_RED = 'on_red'
ON_GREEN = 'on_green'
ON_YELLOW = 'on_yellow'
ON_BLUE = 'on_blue'
ON_MAGENTA = 'on_magenta'
ON_CYAN = 'on_cyan'
ON_WHITE = 'on_white'

BOLD = 'bold'
DARK = 'dark'
UNDERLINE = 'underline'
BLINK = 'blink'
REVERSE = 'reverse'
CONCEALED = 'concealed'
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
def label_print(msg, num_of_new_lines=0, num_of_tabs=0,
                color=None, label="LABEL: ", timestamp=True,
                exception=None):
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
def output_print(msg, num_of_new_lines=0, num_of_tabs=0,
                 color=INFO_COLOR, output_label=" >> ",
                 timestamp=True, exception=None):
    """VOID : Print out an output message with a nice format"""
    # output print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=output_label, timestamp=timestamp,
                exception=exception)


@se
def error_print(msg, num_of_new_lines=0, num_of_tabs=0,
                color=ERROR_COLOR, error_label="* * * ERROR * * * : ",
                timestamp=True, exception=None):
    """VOID : Print out an error message with a nice format"""
    # error print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=error_label, timestamp=timestamp,
                exception=exception)


@se
def warning_print(msg, num_of_new_lines=0, num_of_tabs=0,
                  color=WARNING_COLOR, warning_label="* WARNING * : ",
                  timestamp=True, exception=None):
    """VOID : Print out a warning message with a nice format"""
    # warning print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=warning_label, timestamp=timestamp,
                exception=exception)


@se
def info_print(msg, num_of_new_lines=0, num_of_tabs=0,
               color=INFO_COLOR, info_label="INFO : ",
               timestamp=True, exception=None):
    """VOID : Print out an info message with a nice format"""
    # info print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=info_label, timestamp=timestamp,
                exception=exception)


@se
def success_print(msg, num_of_new_lines=0, num_of_tabs=0,
                  color=SUCCESS_COLOR, success_label="SUCCESS : ",
                  timestamp=True, exception=None):
    """VOID : Print out a success message with a nice format"""
    # success print
    label_print(msg, num_of_new_lines=num_of_new_lines,
                num_of_tabs=num_of_tabs, color=color,
                label=success_label, timestamp=timestamp,
                exception=exception)


@nocrash_return
def error_format(msg, num_of_new_lines=0, num_of_tabs=0,
                 label="* * * ERROR * * *: ", timestamp=True,
                 exception=None):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


@nocrash_return
def warning_format(msg, num_of_new_lines=0, num_of_tabs=0,
                   label="* WARNING *: ", timestamp=True,
                   exception=None):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


@nocrash_return
def success_format(msg, num_of_new_lines=0, num_of_tabs=0,
                   label="SUCCESS: ", timestamp=True,
                   exception=None):
    """RETURN : Return a string formatted in a LABEL way"""
    label_format(msg, num_of_new_lines=num_of_new_lines,
                 num_of_tabs=num_of_tabs,
                 label=label, timestamp=timestamp,
                 exception=exception)


def list_format(list_to_format, intro_label="Printing the list:",
                color=WHITE, show_debug=True):
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


def dict_format(dict_to_format, intro_label="Printing the dict:",
                color=WHITE, show_debug=True):
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
def list_print(list_to_print, intro_label="Printing the list:",
               color=WHITE, show_length=True, show_debug=True):
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
def dict_print(dict_to_print, intro_label="Printing the dict:",
               color=WHITE, show_debug=True):
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
def input_color(msg, color, parse_none=False,
                show_debug=True):
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
def ask_input_int(msg, to_bool=False, color=None,
                  security_stop=1000, show_debug=True):
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
def ask_input_login(pre_msg="", color=None,
                    username_label="USERNAME",
                    password_label="PASSWORD",
                    pin_label=None,
                    show_debug=False):
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


# + + + + + CAST + + + + +
@nocrash_return
def str_to_int(string, show_debug=True):
    """RETURN : {'status': True/False, 'value': value, 'error': error_msg}"""
    try:
        to_int = int(string)
        return {"status": True, "value": to_int, "error": ""}
    except Exception as e:
        if show_debug:
            error_print("Cannot cast string to integer", exception=e)
        return {"status": False, "value": None, "error": "Cannot cast string to integer because -> {}".format(str(e))}


# - - NAME STANDARDS - -
@nocrash_return
def to_schema(client_name):
    """RETURN : the schema (ex: By Humankind -> byhumankind) from client_name"""
    return str(client_name).lower().replace('_', '').replace(' ', '').strip()


@nocrash_return
def to_client(client_name):
    """RETURN : the client (ex: By Humankind -> by_humankind) from client_name"""
    return str(client_name).lower().replace(' ', '_').strip()


@nocrash_return
def to_s3_bucket_name(client_name, addendum='-sgs'):
    """RETURN : the client (ex: By Humankind -> byhumankind-sgs) from client_name"""
    return (to_schema(str(client_name)) + addendum).strip()


@nocrash_return
def to_s3_bucket(client_name, addendum='-sgs'):
    """RETURN : the client (ex: By Humankind -> byhumankind-sgs) from client_name"""
    return (to_schema(str(client_name)) + addendum).strip()
# - - NAME STANDARDS - -

# - - TO CAST [NO CRASH] - -
@nocrash_return
def to_int(object):
    """RETURN : None if unable to convert to int or int"""
    return int(object)


@nocrash_return
def to_str(object):
    """RETURN : None if unable to convert to str or str"""
    return str(object)
# - - TO CAST [NO CRASH] - -

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
def generate_db_cols_from_df(df, pk=None, sortkey=None, encode='zstd'):
    all_cols = list(df.columns)
    cols_float = list(df.select_dtypes(include=['float64']).columns)
    cols_str = list(df.select_dtypes(include=['object']).columns)
    cols_int = list(df.select_dtypes(include=['int']).columns)
    cols_bool = list(df.select_dtypes(include=['bool']).columns)
    cols_datetime_tz = list(df.select_dtypes(include=['datetime64[ns, UTC]']).columns)
    cols_datetime = list(df.select_dtypes(include=['datetime64[ns]']).columns)
    # prepare statement
    list_cols = []
    for i in range(len(all_cols)):
        if i == len(all_cols) - 1:
            # check type
            if all_cols[i] in cols_datetime_tz:
                type_to_use = 'timestamptz'
            elif all_cols[i] in cols_datetime:
                type_to_use = 'timestamp'
            elif all_cols[i] in cols_float:
                type_to_use = 'float'
            elif all_cols[i] in cols_str:
                type_to_use = 'varchar'
            elif all_cols[i] in cols_bool:
                type_to_use = 'bool'
            elif all_cols[i] in cols_int:
                type_to_use = 'integer'
            # stmt
            stmt = ' '.join((all_cols[i], type_to_use))
            if encode is not None:
                stmt += f' encode {encode}'
            if pk is not None or sortkey is not None:
                if pk is not None:
                    if all_cols[i] == pk:
                        if encode is not None:
                            stmt = stmt.replace(f' encode {encode}', ' primary key')
                        else:
                            stmt += ' primary key'
                else:
                    if all_cols[i] == sortkey:
                        if encode is not None:
                            stmt = stmt.replace(f' encode {encode}', ' sortkey')
                        else:
                            stmt += ' sortkey'
            list_cols.append(stmt)
        else:
            # check type
            if all_cols[i] in cols_datetime_tz:
                type_to_use = 'timestamptz'
            elif all_cols[i] in cols_datetime:
                type_to_use = 'timestamp'
            elif all_cols[i] in cols_float:
                type_to_use = 'float'
            elif all_cols[i] in cols_str:
                type_to_use = 'varchar'
            elif all_cols[i] in cols_bool:
                type_to_use = 'bool'
            elif all_cols[i] in cols_int:
                type_to_use = 'integer'
            # stmt
            stmt = ' '.join((all_cols[i], type_to_use))
            if encode is not None:
                    stmt += f' encode {encode}'
            if pk is not None or sortkey is not None:
                if pk is not None:
                    if all_cols[i] == pk:
                        if encode is not None:
                            stmt = stmt.replace(f' encode {encode}', ' primary key')
                        else:
                            stmt += ' primary key'
                else:
                    if all_cols[i] == sortkey:
                        if encode is not None:
                            stmt = stmt.replace(f' encode {encode}', ' sortkey')
                        else:
                            stmt += ' sortkey'
                
            stmt += ',\n'
            list_cols.append(stmt)
    list_cols = ''.join(list_cols)
    cols_stmt = f"""(
        {list_cols}
    );
    """
    return cols_stmt


@nocrash_return
def correct_filepath(string):
    """RETURN : The file path with '/' at the end
    if the developer/user forgot it"""
    string = string + '/' if string[-1] != '/' else string
    return string


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


@nocrash_return
def progress_bar(type="ChargingBar", steps=20):
    """RETURN : A progress bar object"""
    if type == "ChargingBar":
        bar = ChargingBar('Processing', max=steps)
    else:
        bar = Bar('Processing', max=steps)

    return bar

@nocrash_void
def insert_cronjob(
    cronjob_section,
    cronjob_string,
    cronjob_filepath='/home/ec2-user/cronjobs/crontab_config',
    where="END"
):
    """VOID : Insert a cronjob"""
    with open(cronjob_filepath, 'r') as f:
        content = f.read()
    
    # replace and insert new cronjob
    content = content.replace(f'# - - - {where} {cronjob_section} - - -', f'{cronjob_string}\n# - - - {where} {cronjob_section} - - -')

    # write new crontab file
    with open(cronjob_filepath, 'w') as f:
        f.write(content)
    
    success_print("Cronjob inserted")

@nocrash_void
def remove_cronjob(
    cronjob_string,
    cronjob_filepath='/home/ec2-user/cronjobs/crontab_config'
):
    """VOID : Remove a cronjob"""
    with open(cronjob_filepath, 'r') as f:
        content = f.read()
    
    # replace and insert new cronjob
    content = content.replace(f'{cronjob_string}\n', '')

    # write new crontab file
    with open(cronjob_filepath, 'w') as f:
        f.write(content)
    
    success_print("Cronjob removed")

@nocrash_return
def get_cronjobs(
    cronjob_section,
    cronjob_filepath='/home/ec2-user/cronjobs/crontab_config'
):
    """VOID : Get all cronjobs under a section"""
    with open(cronjob_filepath, 'r') as f:
        content = f.read()
    
    # split based on START
    content = content.split(f'# - - - START {cronjob_section} - - -')[1]
    content = content.split(f'# - - - END {cronjob_section} - - -')[0]
    content = content.split('\n')
    content = [cron for cron in content if cron != '']

    return content
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


def process(
    instructions, interrupt=True,
    wait_time=0.5,
    show_debug=True
):
    """
    RETURN :  {"status": True/False dict, "error": error_msg dict, "value": value dict},
               perform a function

    Parameters
    ----------
    instructions : a list (of dicts)
        The list of dicts to execute
    interrupt : bool
        If error is present then interrupt process
    show_debug : bool
        Show debug info?
    wait_time : float
        The wait time between 2 actions

    Returns
    -------
    result :  {"status": True/False dict, "error": error_msg dict, "value": value dict}
    """
    try:
        # prepare status, errors, values dicts
        status, errors, values = {}, {}, {}
        iteration = 1
        new_line()
        bar = progress_bar(steps=len(instructions))
        time_init = 0
        # iterate on instrctions
        for instruction in instructions:
            # wait
            time.sleep(wait_time)
            if show_debug:
                label_print(
                    "\n- - - - EXECUTE {}/{}: '{}', function -> {} - - - -\n".format(str(iteration), str(len(instructions)), str(instruction["name"]), instruction["function"].__name__),
                    label="",
                    color=MAGENTA,
                    num_of_new_lines=1
                )
                time_step = "NA" if time_init == 0 else time.time() - time_init
                remaining_time = "NA" if time_step == "NA" else round((len(instructions) - iteration)*time_step, 3)
                min_remaining = "NA" if time_step == "NA" else round(remaining_time/60, 3)
                hour_remaining = "NA" if time_step == "NA" else round(min_remaining/60, 3)
                bar.next()
                new_line()
                info_print("Remaining time : {} sec / {} mins / {} hours\n".format(str(remaining_time), str(min_remaining), str(hour_remaining)), timestamp=False, color=BLUE)
            # perform function
            action = perform(instruction["function"], instruction["kwargs"], instruction["args"], show_debug=show_debug)
            # collect info
            status[iteration], errors[iteration], values[iteration] = (
                (instruction["name"], action["status"]),
                (instruction["name"], action["error"]),
                (instruction["name"], action["value"])
            )
            if action["status"]:
                pass
            else:
                if interrupt:
                    if show_debug:
                        error_print("Error in process {}/{} function chain '{}' -> ".format(str(iteration), str(len(instructions)), str(instruction["name"])) + action["error"])
                        warning_print("Interrupting process because interrupt=True...")
                    return {"status": status, "error":  errors, "value": values}
                else:
                    pass
            # end
            iteration += 1
            # time init
            time_init = time.time()
            if show_debug:
                print_color("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n", color=MAGENTA)

        bar.finish()
        if show_debug:
            success_print("Congrats, process run successfully!")
        return {"status": status, "error":   errors, "value": values}
    except (Exception, KeyboardInterrupt) as e:
        if show_debug:
            warning_print("Error during process!", exception=e)
        return {"status": status, "error":   errors, "value": values}
# + + + + + PROCESSES/CHAINS + + + + +
# * * * * * * * * * * FUNCTIONS * * * * * * * * * *
