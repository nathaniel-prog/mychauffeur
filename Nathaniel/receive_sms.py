import os
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse





app= Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def send_sms():
    resp=MessagingResponse()
    resp.message('il est temps !!')


    return str(resp)



send_sms()
send_sms()

if __name__ == '__main__':
    app.run(debug=True)


