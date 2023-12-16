import smtplib
import ssl


def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465
    username = "rob.kelly.python@gmail.com"
    password = "vsvwdjkprlqjywgj"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)

