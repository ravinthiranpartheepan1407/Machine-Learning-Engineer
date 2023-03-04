import smtplib
from pathlib import Path
from string import Template
email = input("Enter Your Email: ")
message = input("Enter Your Message: ")
content = input("Enter Your Content: ")
html = Template(Path("./email_html/index.html"))

env = {
    "username": "dummypythoncode@gmail.com",
    "password": "Dummy@619"
}

env_alt = ["dummypythoncode@gmail.com", "Dummy@619*"]

# smtp.helo / smtp.ehlo -> Are same which is used to get greet message once connection is established
# smtp.starttls -> Used to establish secure connection via TLS

# Port 587 used commonly
def email(email, message, content):
    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.helo()
            smtp.starttls()
            smtp.login(list(env.keys()[0]), list(env.keys()[1]))
            smtp.send_message(email, message, content)
            print("Message Sent")
    except:
        raise smtplib.SMTPAuthenticationError("Credentials Not Correct Dude!")

email(email, message, content)

def send_email_html(email, message, html):
    wrap_html = html.substitute({'name': 'ravi'})
    try:
        with smtplib.SMTP(host='smt.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(env_alt[0], env_alt[1])
            smtp.send_message(email, message, wrap_html)
    except:
        raise smtplib.SMTPConnectError("Can't establish connection dude!")
