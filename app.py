from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Hugging Face token (keep it secret)
HUGGINGFACE_API_TOKEN = "your_huggingface_token_here"
MODEL_NAME = "google/flan-t5-base"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.get_json().get('query', '')

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
    }

    payload = {
        "inputs": f"Question: {user_input} Answer:",
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
        }
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()

        # Hugging Face response format is a list of dictionaries
        if isinstance(result, list) and 'generated_text' in result[0]:
            answer = result[0]['generated_text']
        else:
            answer = "Sorry, I couldn't generate a response."

        return jsonify({'response': answer})

    except requests.exceptions.RequestException as e:
        return jsonify({'response': f"API request failed: {str(e)}"})
