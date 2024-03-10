from flask import Flask, jsonify
import string
import random
import datetime

app = Flask(__name__)


def generate_random_string(string_length):
    """
    Generates a random string of string_length size
    :param string_length:
    :return random_string:
    """
    all_alphanum_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    len_alphanum_chars = len(all_alphanum_chars)

    return "".join([all_alphanum_chars[random.randint(0, len_alphanum_chars - 1)] for _ in range(string_length)])


@app.route('/')
def show_timestamp():
    """
    Endpoint to show current timestamp
    """
    current_time = datetime.datetime.now()
    random_str = generate_random_string(10)

    return jsonify({'timestamp': current_time.isoformat(),
                    'random_str': random_str})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

