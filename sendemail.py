# Program to send Email by using Program.
# We required the smtplib module and smtpdomain name for mail and port number.
import smtplib
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.ehlo() # Connection with gmail server
connection.starttls() # start transportation of msg at Transport layer
connection.login("shompower007@gmail.com","myintern@123")
connection.sendmail("shompower007@gmail.com","goudtarun007@gmail.com","hi this is tarun")
connection.quit()


