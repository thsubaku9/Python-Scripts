#Enable access to SMTP form your respective email account, or else the script won't work
import smtplib
import getpass 
maillst={'gmail':'smtp.gmail.com','hotmail':'smtp-mail.outlook.com','yahoo':'smtp.mail.yahoo.com','comcast':'smtp.comcast.net','at&t':'smpt.mail.att.net','verizon':'smtp.verizon.net'}
for i in maillst.keys():
	print (i)
	
name=input('Enter account type')

mail=maillst[name]
port_values=[587,465]

try:
    smtpObj = smtplib.SMTP(mail, port_values[0])
except:
    smtpObj = smtplib.SMTP_SSL(mail,port_values[1])

smtpObj.ehlo()
smtpObj.starttls()

user=input("Enter username\t")
password=getpass.getpass("Password\t")
smtpObj.login(user,password)
subj=input("\nEnter subject\n")
subj="Subject: "+subj +"\n"
text=input("\nEnter text\n")
textsend=subj+""+text
to=input("\nEnter recepient")
smtpObj.sendmail(user,to,textsend)
smtpObj.close()

