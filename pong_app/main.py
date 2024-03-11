from flask import Flask, jsonify

app = Flask(__name__)

class Counter:
    value = 0

    @classmethod
    def increment(self):
        self.value += 1
        return self.value

@app.route('/pingpong')
def pingpong():
    count = Counter.increment()
    return jsonify({'counter': count})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)