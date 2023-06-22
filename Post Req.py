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