import streamlit as st
import requests
import json

# Define the URL and API key for your Azure REST API
url = 'https://chatbot-ierzc.northeurope.inference.ml.azure.com/score'
api_key = 'ZBOmGtdwONwlxnHTyItY70TmuL3qUTaF'

# Define a function to send a message to the chatbot API and get a response
def send_message(message):
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

    return answer

# Set the title of the web app
st.title('Chatbot')

# Define a text input field for the user to enter their message
message = st.text_input('Enter your message')

# If the user has entered a message, send it to the chatbot API and display the response
if message:
    answer = send_message(message)
    st.write('Chatbot: ' + answer)