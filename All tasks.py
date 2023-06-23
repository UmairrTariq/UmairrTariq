# Task A and C

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





# Task B



import requests

order_id = '12345'
date = '22-jun-2023'  # Replace with the order ID obtained from the number variable in Dialogflow

# Make a POST request to fetch the shipment date
response = requests.post('https://7d78-202-123-240-28.ngrok.io/webhook', json={'queryResult': {'intent': {'displayName': 'process'}, 'parameters': {'number': order_id, 'date': date}}})

# Rest of the code remains the same


# Check the response status code
if response.status_code == 200:
    try:
        response_data = response.json()
        fulfillment_messages = response_data['fulfillmentMessages']
        if fulfillment_messages:
            fulfillment_text = fulfillment_messages[0]['text']['text'][0]
            print(f"Shipment date is : {fulfillment_text[36:]}")
        else:
            print("No fulfillment messages found in the response.")
    except ValueError:
        print("Failed to parse the response as JSON.")
        print(f"Response Content: {response.content}")
    except KeyError:
        print("The response does not contain the expected fields.")
else:
    print("Failed to fetch the fulfillment messages.")