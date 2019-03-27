from smtplib import SMTP
from email.mime.text import MIMEText as text

def send_email(mail_domain, login, password, sender, recipient):
    """
    Send email from one email to another using following parameters
    :param mail_domain:email server domain name you want login to
    :param login: login name
    :param password: password
    :param sender: send from
    :param recipient: send to
    :return: None
    """
    with SMTP(mail_domain, 587) as smtp:
        smtp.starttls()
        smtp.login(login, password)
        m = text("I did it!")
        m["Subject"] = "Message from Vadym Rovenko"
        smtp.sendmail(sender,recipient, m.as_string())


if __name__ == "__main__":
    send_email("smtp.gmail.com", "sspavl21@gmail.com", "*********", "sspavl21@gmail.com", "el.piankova@gmail.com")


