import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("sspavl21@gmail.com", "QAZxsw123")
a = mail.list()
b = mail.select("INBOX")
print(a)
print(b)

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")

raw_email = data[0][1]

email_message = email.message_from_bytes(raw_email)

print(email_message["To"])
print(email.utils.parseaddr(email_message["From"]))
for i in email_message.items():
    print(i)

def get_text_block(email_message_item):
    """
    Method take text block from the EmailMessage object
    :param email_message_item: emailMassage object
    :return: text from the message
    """
    maintype = email_message_item.get_content_maintype()
    if maintype == "multipart":
        for part in email_message_item.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == "text":
        return email_message_item.get_payload()

m = get_text_block(email_message)
print(m)
