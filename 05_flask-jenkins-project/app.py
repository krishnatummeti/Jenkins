from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask CI/CD Demo!"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
