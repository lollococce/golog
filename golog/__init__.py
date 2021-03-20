# import submodules you want to install
from .decorators import (
    timer,
    deprecated,
    se,
    sev,
    nocrash_return,
    nocrash_void
)
from .tools import (
    perform,
    frequency_elements,
    is_anagram,
    filepath_exists,
    correct_filepath,
    correct_nonlist,
    dict_stringify,
    json_stringify,
    decode_length_delta,
    is_dict,
    is_list,
    is_int,
    is_str,
    is_url,
    to_dict,
    to_list,
    to_int,
    to_set,
    to_str
)
from .log import (
    HOME,
    label_format,
    label_print,
    output_print,
    error_print,
    warning_print,
    info_print,
    success_print,
    error_format,
    warning_format,
    success_format,
    list_format,
    dict_format,
    list_print,
    dict_print,
    print_color,
    print_magenta,
    print_green,
    print_red,
    print_yellow,
    print_blue,
    welcome,
    new_line,
    new_lines,
    input_color,
    ask_input_int,
    ask_input_login,
    ask_password
)
from .alerts import (
    Slack,
    Twilio,
    send_process,
    error,
    critical,
    success,
    info,
    debug,
    warning
)


__docformat__ = "restructuredtext"

__version__ = '0.1.0'

# module level doc-string
__doc__ = """
golog - a powerful general logging and monitoring library for Python
=====================================================================

**golog** is a Python package providing many different useful functions

Main Features
-------------
Here are just a few of the things that golog does well:
  - Nice Logging
  - Integrated Alerts (Slack, Email , SMS)
  - Useful Decorators
  - Tools to make your code nicer and more reliable
"""
