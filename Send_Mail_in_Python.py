import smtplib
content = 'hello world this mail is sent through my py code'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('Email ID','PSWD')
mail.sendmail('FROM','TO',content)
mail.close()
