'''
Notes: The program it sent the mail succefully.
The only problem was that it cannot sppoof the mail address with the google service
Most known servers today do not allow e-mail spoofing.
To do some real phishing, try to use gophish instead of python.
PHP, and SMTP they're also good to spoof the email

Check some pages
https://security.stackexchange.com/questions/137780/can-i-spoof-email/137791
https://github.com/gophish/gophish/issues/1044
https://www.digitalshadows.com/blog-and-research/security-practitioners-guide-to-email-spoofing-and-risk-reduction/
'''

import smtplib      #Module to use to send the mails
import ssl          #To create ssl context

def send_mail(sender_mail,password,from_mail,to_mail,message):
    port = 465                                          #For SSl
    context = ssl.create_default_context()              #Create SSL context for secure mail
    server = smtplib.SMTP_SSL(host='smtp.google.com', port=port, context=context)
    server.login(sender_mail, password)
    server.sendmail(from_mail,to_mail,message)
    print("Mail sent")
    server.quit()                                       #Quit the server


if __name__ == "__main__":
    #Get credentials
    sender_mail = input("[+] Enter your mail: ")                #Attacker real mail
    password = input("[+] Enter your password: ")               #Real mail password
    from_mail = input("[+] Enter your spoof mail: ")            #Spoof attacker real mail
    from_name = input("[+] Enter your spoof name: ")            #Spoof attacker name
    subject = input("[+] Enter your name subject: ")            #Mail Subject
    to_mail = input("[+] Enter your target mail: ")             #Email content
    message = f'''
From: {from_name} <{from_mail}>
To: {to_mail}
Subject: {subject}

Hello, this is a sending test
'''
    send_mail(sender_mail,password,from_mail,to_mail,message)             #Send the mail