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
from .log import *
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
    """RETURN : None if unable to convert to int or int"""
    return int(object)


@nocrash_return
def to_str(object):
    """RETURN : None if unable to convert to str or str"""
    return str(object)


@nocrash_return
def to_list(object):
    """RETURN : None if unable to convert to int or int"""
    return list(object)
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
def correct_filepath(string, slash_remove=False):
    """RETURN : The file path with '/' at the end
    if the developer/user forgot it or viceversa"""
    if slash_remove:
        string = str(string) + '/' if string[-1] != '/' else str(string)[:-1]
    else:
        string = str(string) + '/' if string[-1] != '/' else string
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


@nocrash_void
def insert_cronjob(
    cronjob_section,
    cronjob_string,
    cronjob_filepath,
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
# + + + + + Functions + + + + +

