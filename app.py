from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Sneha 🚀 Welcome to your first Flask app!"

@app.route('/about')
def about():
    return "This is a small project created using Flask."

if __name__ == '__main__':
    app.run(debug=True)
