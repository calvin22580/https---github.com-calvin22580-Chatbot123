import streamlit as st
import requests
import json

# Set the width of the output window
st.set_page_config(layout="wide")

# Define the URL of the chatbot API
url = 'https://chatbot-dcqxa.northeurope.inference.ml.azure.com/score'

# Define the API key for the chatbot API
api_key = 'g0O1T9GKcF2BtmcPscWTm83NYQq6xwDk'

# Define a function to send a message to the chatbot API and get a response
def send_message(message, max_length=10000):
    # Construct the request data as a dictionary
    data = {"question": message}

    # Encode the data as JSON
    body = json.dumps(data)

    # Define the headers for the request
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'blue' }

    # Send a POST request to the Azure REST API
    response = requests.post(url, headers=headers, data=body)

    # Parse the response JSON and extract the answer
    answer = response.json()['answer']

    # Truncate the answer if it exceeds the maximum length
    if len(answer) > max_length:
        answer = answer[:max_length] + '...'
        print(f'Truncated answer to {max_length} characters')

    print(f'Answer length: {len(answer)}')

    return answer

# Set the title of the web app
st.title('Chatbot')

# Define a text input field for the user to enter their message
message = st.text_input('Enter your message')

# If the user has entered a message, send it to the chatbot API and display the response
if message:
    answer = send_message(message)
    st.write('Chatbot: ' + answer)