import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendgridmail():
    message = Mail(
        from_email='abitha.thangadurai@gmail.com',
        to_emails='sherrly24052003@gmail,com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send()
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)