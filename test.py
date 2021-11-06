# import imaplib, re
# pattern_uid = re.compile(r'\d+ \(UID (?P<uid>\d+)\)')

# import email

# def connect(email):
#     imap = imaplib.IMAP4_SSL("imap.gmail.com")
#     password = 'lbxtkujxdxyhscsz'
#     imap.login(email, password)
#     return imap

# def disconnect(imap):
#     imap.logout()

# def parse_uid(data):
#     match = pattern_uid.match(data)
#     return match.group('uid')

# # from imap_tools import MailBox, A
# # with MailBox('imap.gmail.com').login('mr.santa.bot@gmail.com', 'lbxtkujxdxyhscsz', 'INBOX') as mailbox:
# #     for msg in mailbox.fetch(A(all=True)):
# #         sender = msg.from_
# #         body = msg.text or msg.html
# #         count = 0
# #         for att in msg.attachments:
# #             print(att.payload)
# #             count +=1 
# #         print(count)


# from mailer import Mailer

# mail = Mailer(email='mr.santa.bot@gmail.com',
#               password='lbxtkujxdxyhscsz')

# mail.send(receiver='davide1936@gmail.com',  # Email From Any service Provider
#           subject='TEST',
#           message='HI, This Message From Python :)')