import smtplib

smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
print(type(smtpObj))

print(smtpObj.ehlo())

print(smtpObj.starttls())
smtpObj.login('amith.reddym@hotmail.com', 'amithM423')

smtpObj.sendmail('amith.reddym@hotmail.com', 'amith.reddy.mekala@accenture.com', \
                  'Subject: test email \n hello Amith')

smtpObj.quit()
