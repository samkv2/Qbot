
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    if 'start quiz' in incoming_msg:
        resp.message("Welcome to the Quiz! Here's your first question: What is 2 + 2?")
    elif '4' in incoming_msg:
        resp.message("Correct! Your score is 1. Next question: What is the capital of France?")
    else:
        resp.message("Incorrect! Try again.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
