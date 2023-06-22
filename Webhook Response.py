from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Receive the WebhookRequest from the bot
    webhook_request = request.get_json(force=True)

    # Extract the intent name from the webhook request
    intent_name = webhook_request['queryResult']['intent']['displayName']

    # Define the default welcome response
    if intent_name == 'Default Welcome Intent':
        name = webhook_request['queryResult']['parameters']['name']
        fulfillment_text = f"Hi! This is {name}'s bot. How can I help you?"

    # Define the order intent response
    elif intent_name == 'order':
        fulfillment_text = "Can I check your order ID?"

    # Define the process intent response
    elif intent_name == 'process':
        number = webhook_request['queryResult']['parameters']['number']
        date = webhook_request['queryResult']['parameters']['date']
        fulfillment_text = f"Your order {number} will be shipped on {date}."

    # Define the welcome intent response
    elif intent_name == 'welcome':
        fulfillment_text = "You're welcome."

    # Handle unrecognized intents
    else:
        fulfillment_text = "Sorry, I didn't understand that."

    # Create the WebhookResponse
    webhook_response = {
        'fulfillmentMessages': [
            {
                'text': {
                    'text': [fulfillment_text]
                }
            }
        ]
    }
    print(fulfillment_text)

    # Convert the response to JSON string
    response_json = json.dumps(webhook_response)

    # Set the content type as application/json
    response = app.response_class(
        response=response_json,
        status=200,
        mimetype='application/json'
    )

    # Return the response
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
