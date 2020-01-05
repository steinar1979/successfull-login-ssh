import smtplib, ssl
  
class Sendmail:


    def __init__(self, username, password, smtpserver, port):
        self.un = username
        self.pwd = password
        self.port = port
        self.smtps = smtpserver

    def sendMail(self, sender_email, rec_email, msg):
        s = smtplib.SMTP(self.smtps, self.port)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(self.un, self.pwd)

        # message to be sent
        message = msg

        # sending the mail
        s.sendmail(sender_email, rec_email, message)

        # terminating the session
        s.quit()
