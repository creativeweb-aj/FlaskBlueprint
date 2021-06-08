import datetime
from App.Api.models import User, EmailHandler
from App.extension import db
from flask import render_template_string
from flask_mail import Message
import uuid
import smtplib
import os


class EmailService:
    def saveEmail(self, user):
        subject = "Creative Web Verify Your Email"
        key = str(uuid.uuid4())
        url = "http://localhost:5000/email/verify?id=" + key
        body = render_template_string("Hello, This is you verification link {{ link }}", link=url)
        dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
        obj = EmailHandler(user_id=user.id, subject=subject, body=body, uuid=key,
                           created_on=dateTime, updated_on=dateTime)
        db.session.add(obj)
        db.session.commit()

        self.sendEmail(obj, user)

        return obj

    def sendEmail(self, data, user):
        subject = data.subject
        body = data.body
        email = user.email
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        emailId = os.environ.get('MAIL_USERNAME')
        password = os.environ.get('MAIL_PASSWORD')
        s.login(emailId, password)
        # sending the mail
        s.sendmail(emailId, email, body)
        # terminating the session
        s.quit()
        self.updateEmail(data)
        return data

    def updateEmail(self, data):
        id = data.id
        dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
        emailObj = EmailHandler.query.filter_by(id=id, is_sent=False).first()
        emailObj.is_sent = True
        emailObj.sent_on = dateTime
        emailObj.updated_on = dateTime
        db.session.commit()
        return emailObj