import imaplib

msrvr=imaplib.IMAP4_SSL('imap.gmail.com',993)
unm='easyqa.thinkmobiles@gmail.com'
pwd='ThinkMobiles'
msrvr.login(unm,pwd)
stat,cnt=msrvr.select('Inbox')
stat,dta = msrvr.fetch(cnt[0],'(UID BODY[TEXT])')
email = dta[0][1]
print (email)
print (email)
msrvr.close()
msrvr.logout()
#TEST
msrvr.logout()