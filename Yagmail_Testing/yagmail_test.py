#Make sure you pip install yagmail
import yagmail

from_address = 'shivansh.shukla.ee104@gmail.com' #this is your own gmail account
app_password = 'vnwi kazc zcwr yyya' # a token for gmail, this is the app password from Gmail Security
to_address = 'shivansh.shukla@sjsu.edu'   #send test to another email or the same email is OK

subject = 'Test sending email using yagmail'  #modify the subject line anyway you like
content = ["""Greetings, 
I am Shivansh Shukla. I just want to let you know that now I have my own automated
email service.
Cheers,
Shivansh Shukla"""]  #you can have different email and attachment

with yagmail.SMTP(from_address, app_password) as yag:
    yag.send(to_address, subject, content)
    print('Email is Successfully sent')  #you can have different success message