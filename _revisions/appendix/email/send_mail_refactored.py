import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def mail(fromaddr, toaddr, sub, text, smtp_host, smtp_port, user, password):

    # parts of the actual email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sub
    msg.attach(MIMEText(text))

    # connect to the server
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)

    # initiate communication with server
    server.ehlo()

    # use encryption
    server.starttls()

    # login to the server
    server.login(user, password)

    # send the email
    server.sendmail(fromaddr, toaddr, msg.as_string())

    server.quit()

if __name__ == '__main__':
    fromaddr = 'hermanmu@gmail.com'
    toaddr = 'hermanmu@gmail.com'
    subject = 'test'
    body_text = 'hear me?'
    smtp_host = 'smtp.gmail.com'
    smtp_port = '587'
    user = 'hermanmu@gmail.com'
    password = "it's a secret - sorry"

    mail(fromaddr, toaddr, subject, body_text, smtp_host, smtp_port, user, password)
