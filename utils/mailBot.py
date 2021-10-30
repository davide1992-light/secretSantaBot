import smtplib
import email 

class MailBot:
    def __init__(self, username, password, smtpServer, smtpPort):
        self.smtp = smtplib.SMTP(smtpServer, smtpPort)
        self.smtp.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        self.smtp.starttls() #Puts connection to SMTP server in TLS mode
        self.smtp.ehlo()
        self.smtp.login(username, password)
        
        self.username = username

    
    def send_mail(self, text, subject, receiver):
        msg = email.message_from_string(text)
        msg['From'] = self.username
        msg['To'] = receiver
        msg['Subject'] = subject
        self.smtp.sendmail(self.username, receiver, msg.as_string())
