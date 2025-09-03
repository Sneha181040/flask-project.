from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Hello, Sneha 🚀 Welcome to your first Flask app!"})

# About route with JSON response
@app.route('/about')
def about():
    return jsonify({
        "name": "Sneha Ghatol",
        "age": 21,
        "field": "Artificial Intelligence & Data Science",
        "college": "PVGCOESSDIOM"
    })

# Example POST route
@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get("Name", "Guest")
    return jsonify({"message": f"Hello {name}, nice to meet you!"})

# Example HTML template route
@app.route('/profile')
def profile():
    return render_template("profile.html",
                           name="Sneha Ghatol",
                           age=21,
                           field="AI & Data Science",
                           college="PVGCOESSDIOM")

if __name__ == '__main__':
    app.run(debug=True)
