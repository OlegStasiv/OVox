import imaplib

def get_unread_email():

    msrvr=imaplib.IMAP4_SSL('imap.gmail.com',993)
    unm='easyqa.thinkmobiles@gmail.com'
    pwd='ThinkMobiles'
    msrvr.login(unm,pwd)
    stat,cnt=msrvr.select('Inbox')
    stat,dta = msrvr.fetch(cnt[0],'(UID BODY[TEXT])')
    email_content = dta[0][1]
    print (email_content)
    msrvr.close()
    msrvr.logout()
    return email_content