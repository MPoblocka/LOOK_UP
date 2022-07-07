# Look-Up-
LOOK UP is a program that send you a text massage to "look up" if the International Space Satellite (ISS) is currently in sight around your location.

LOOK UP is written in PyCharm using Python programming language. 
It takes advantage of API requested from http://open-notify.org which allows to check the current ISS location and compares it with curent location of the user. The user's location is defined using https://sunrise-sunset.org/ API. 

The notification email is sent to the user using Python's smtplib module which defines an SMTP client session object that can be used to send email to destination address with an SMTP or ESMTP listener daemon.
