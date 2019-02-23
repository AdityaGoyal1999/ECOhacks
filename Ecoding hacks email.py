""" This python class is to send email to the user about his check list
activities."""

import smtplib
from email.message import EmailMessage
import Ecohacks

def send_email() -> None:
    """ sends the recovery email to the user.

    The email login is encrypted.
    Precondition: this functionality is only available to the gmail users
    """
    content.set_content(_content)
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls()
    mail.login(email, password)
    content = ""
    for i in Ecohacks.StreakManager.streaks:
        content += i, "\t", str(i[1])+"\n"
    mail.send_message(content, email, email)
    mail.close()
