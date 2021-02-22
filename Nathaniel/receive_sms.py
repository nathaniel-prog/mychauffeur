import os
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse






app= Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def send_sms(request=None):
    while request is not None:
        resp.message('il est temps !!')

    resp=MessagingResponse()



    return str(resp)



send_sms()
send_sms()

if __name__ == '__main__':
    app.run(debug=True)


