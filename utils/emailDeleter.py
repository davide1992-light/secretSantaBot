from imap_tools import MailBox


def deleteAllSentEmails(username, password, imap_server, subject_to_delete):
    with MailBox(imap_server).login(username, password) as mailbox:
        mailbox.folder.set('[Gmail]/Sent Mail')
        mailbox.delete([msg.uid for msg in mailbox.fetch() if msg.subject==subject_to_delete])
        mailbox.folder.set('[Gmail]/Trash')
        mailbox.delete([msg.uid for msg in mailbox.fetch() if msg.subject==subject_to_delete])
        
