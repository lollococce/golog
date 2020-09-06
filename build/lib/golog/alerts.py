"""
golog alerts
------------
This script contains
functions to alert

Date: 2019-01-29

Author: Lorenzo Coacci
"""
# + + + + + Libraries + + + + +
# import basic
#from .log import *
# to manage slack API
from slack import WebClient
# to manage Twilio API (SMS)
from twilio.rest import Client
# + + + + + Libraries + + + + +


# + + + + + Functions + + + + +
# + + + + + SLACK + + + + +

# + + + + + SLACK + + + + +

# + + + + + SMS + + + + +
class Twilio:
    def __init__(
        self,
        twilio_api_token,
        account_sid,
        from_tel,
        show_debug=False
    ):
        # Initialize the twilio client
        self.account_sid = account_sid
        self.twilio_api_token = twilio_api_token
        twilio_client = Client(
            self.account_sid,
            self.twilio_api_token
        )
        self.twilio_client = twilio_client
        self.from_tel = from_tel
        self.show_debug = show_debug
    

    @se
    def send_sms(self, message, send_to, from_tel=None):
        """
        RETURN : {"status": True/False, "error": error_msg},
                 send a slack message
    
        Parameters
        ----------
        message : string
            The sms message body
        send_to : string
            The string containing the number to send the msg to
        from_tel (optional): string
            The string  containing the number that sends the msg
    
        Returns
        -------
        result : {"status": True/False, "error": error_msg}
        """
        if self.twilio_client is None:
            err_msg = "twilio_client cannot be None and must" \
                      "be specified if you did not input the twilio_client"
            error_print(err_msg)
            return {
                "status": False,
                "error": err_msg
            }
        if from_tel is None:
            from_tel = self.from_tel

        # send message SMS
        message = self.twilio_client.messages.create(
            body=message,
            from_=from_tel,
            to=send_to
        )
        # is sent?
        if self.show_debug:
            success_print(
                "SMS message sent with Twilio with sid " \
                f"{str(message.sid)}, from {str(from_tel)} to {str(send_to)}"
            )
# + + + + + SMS + + + + +


# + + + + + SEND PROCESSES + + + + +
def send_process(
    msg, label, this_file_name=None,
    exception=None,
    slack_to=None, email_to=None,
    sms_to=None, txt_file_to=None,
    csv_file_to=None, file_to_s3=False,
    show_debug=True, color=WHITE,
    slack_client=None,
    twilio_client=None
):
    """VOID it executes a send process"""
    # - - CLEAN INPUT - -
    # make sure everything is clean
    if this_file_name is None:
        this_file_name = ""
    msg, label, this_file_name = str(msg), str(label), str(this_file_name)
    # clean list
    if slack_to is not None:
        slack_to = slack_to if isinstance(slack_to, list) else [slack_to]
        slack_to = [*map(str, slack_to)]
    if email_to is not None:
        email_to = email_to if isinstance(email_to, list) else [email_to]
        email_to = [*map(str, email_to)]
    if sms_to is not None:
        sms_to = sms_to if isinstance(sms_to, list) else [sms_to]
        sms_to = [*map(str, sms_to)]
    if txt_file_to is not None:
        txt_file_to = str(txt_file_to)
        txt_file_to = txt_file_to if txt_file_to[-1] == '/' else txt_file_to + '/'
    if csv_file_to is not None:
        csv_file_to = str(csv_file_to)
        csv_file_to = csv_file_to if csv_file_to[-1] == '/' else csv_file_to + '/'
    # fix path

    try:
        if show_debug:
            pass
    except Exception as err:
        show_debug = True
    # - - CLEAN INPUT - -
    # exception
    e = str(exception) if exception is not None else ""
    # addendum
    addendum = ", EXCEPTION -> {}, TRACEBACK -> {}".format(e, str(traceback.format_exc())) if e != "" else ""
    # label
    label = "{} {}".format(label, this_file_name)
    # message
    message = '[' + str(datetime.now()) + '] ' + label + ' ' + msg + addendum
    # print
    if show_debug:
        label_print(msg + addendum, label=label, timestamp=True, color=color)

    # report via slack
    if slack_to is not None:
        username = label
        # send slack
        result = [
            slack_client.send_slack(message, channel, username, show_debug=show_debug)['status']
            for channel in slack_to
        ]
        if False in result:
            if show_debug:
                warning_print("At least 1 slack message failed during {} process".format(label), timestamp=True)

    # report via email
    if email_to is not None:
        # subject is label
        subject = label
        result = [
            send_email(message, email, subject, show_debug=show_debug)['status']
            for email in email_to
        ]
        if False in result:
            if show_debug:
                warning_print("At least 1 email message failed during {} process".format(label), timestamp=True)

    # report via SMS
    if sms_to is not None:
        result = [
            twilio_client.send_sms(message, tel)['status']
            for tel in sms_to
        ]
        if False in result:
            if show_debug:
                warning_print("At least 1 sms message failed during {} process".format(label), timestamp=True)

    # report to a txt file
    if txt_file_to is not None:
        # define txt name
        txt_file_name = 'log.txt'
        if file_to_s3:
            try:
                with open(txt_file_to + txt_file_name, 'x') as f:
                    f.write(message)
            except Exception as e:
                with open(txt_file_to + txt_file_name, 'a') as f:
                    f.write(message)

            # to s3
            # TO DO: S3 LOAD
            # remove
            os.remove(txt_file_to + txt_file_name)
        else:
            try:
                try:
                    with open(txt_file_to + txt_file_name, 'x') as f:
                        f.write(message + '\n')
                except Exception as e:
                    with open(txt_file_to + txt_file_name, 'a') as f:
                        f.write(message + '\n')
                if show_debug:
                    success_print("log info saved to {}".format(txt_file_to + txt_file_name))
            except Exception as e:
                if show_debug:
                    warning_print("Could not save log info to file {} during {} process, because -> {}".format(txt_file_to + txt_file_name, label, str(e)), timestamp=True)


    # report to a csv file
    if csv_file_to is not None:
        # csv file name
        csv_file_name = 'log.csv'
        if file_to_s3:
            try:
                with open(csv_file_to + csv_file_name, 'x') as f:
                    f.write(message)
            except Exception as e:
                with open(csv_file_to + csv_file_name, 'a') as f:
                    f.write(message)

            # to s3
            # TO DO: S3 LOAD
            # remove
            os.remove(csv_file_to + csv_file_name)
        else:
            try:
                try:
                    with open(csv_file_to + csv_file_name, 'x') as f:
                        f.write(message)
                except Exception as e:
                    with open(csv_file_to + csv_file_name, 'a') as f:
                        f.write(message)
                if show_debug:
                    success_print("log info saved to {}".format(csv_file_to + csv_file_name))
            except Exception as e:
                if show_debug:
                    warning_print("Could not save log info to file {} during {} process, because -> {}".format(txt_file_to + csv_file_name, label, str(e)), timestamp=True)
# + + + + + SEND PROCESSES + + + + +


# + + + + + ERROR PROCESSES + + + + +
def error_process(
    msg, this_file_name=None,
    exception=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=RED
):
    """VOID it executes the error standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="* * * ERROR * * *:",
                 exception=exception,
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + ERROR PROCESSES + + + + +


# + + + + + ERROR PROCESSES + + + + +
def critical_process(
    msg, this_file_name=None, exception=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=RED
):
    """VOID it executes the error standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="! ! ! ! ! CRITICAL ERROR ! ! ! ! !:",
                 exception=exception,
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + ERROR PROCESSES + + + + +


# + + + + + SUCCESS PROCESSES + + + + +
def success_process(
    msg, this_file_name=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=GREEN
):
    """VOID it executes the success standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="SUCCESS:",
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + SUCCESS PROCESSES + + + + +


# + + + + + INFO PROCESSES + + + + +
def info_process(
    msg, this_file_name=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=WHITE
):
    """VOID it executes the info standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="INFO:",
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + INFO PROCESSES + + + + +


# + + + + + DEBUG PROCESSES + + + + +
def debug_process(
    msg, this_file_name=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=WHITE
):
    """VOID it executes the info standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="DEBUG:",
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + DEBUG PROCESSES + + + + +


# + + + + + WARNING PROCESSES + + + + +
def warning(
    msg, this_file_name=None, exception=None,
    slack_to=None, email_to=None, sms_to=None,
    txt_file_to=None, csv_file_to=None, file_to_s3=False,
    show_debug=True, color=YELLOW
):
    """VOID it executes the info standard process"""
    send_process(msg=msg, this_file_name=this_file_name,
                 label="* WARNING *:",
                 exception=exception,
                 slack_to=slack_to,
                 email_to=email_to,
                 sms_to=sms_to,
                 txt_file_to=txt_file_to, csv_file_to=csv_file_to,
                 file_to_s3=file_to_s3,
                 show_debug=show_debug,
                 color=color)
# + + + + + WARNING PROCESSES + + + + +
# + + + + + Functions + + + + +
