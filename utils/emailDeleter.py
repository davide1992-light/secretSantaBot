import imaplib


def deleteAllSentEmails(username, password, imap_server):
    #just a small function that deletes all the emails present in an email box
    with imaplib.IMAP4_SSL(imap_server) as imap:
        imap.login(username, password)
        imap.select("SENT")
        _, messages = imap.search(None, "ALL")
        messages = messages[0].split(b' ')
        for mail in messages:
            if len(mail) != 0:
                imap.store(mail, "+FLAGS", "\\Deleted")
