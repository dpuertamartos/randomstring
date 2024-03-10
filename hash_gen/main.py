# File: random_string_service.py
from flask import Flask, jsonify
import string
import random

app = Flask(__name__)

def generate_random_string(string_length=10):
    """
    Generates a random string of string_length size
    """
    all_alphanum_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    random_str = "".join(random.choice(all_alphanum_chars) for _ in range(string_length))
    return random_str

@app.route('/')
def random_string():
    """
    Endpoint to generate and show a random string
    """
    random_str = generate_random_string()
    timestamp = "Not available"  # Default message in case the file can't be read
    try:
        with open("./files/storage.txt", "r") as f:
            timestamp = f.read().strip()  # Read and strip any leading/trailing whitespace
    except Exception as e:
        print(f"Error reading from storage.txt: {e}")

    return jsonify({'timestamp': timestamp, 'random_string': random_str})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

