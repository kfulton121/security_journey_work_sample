from flask import Flask, render_template, request
import response
import re
    
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/get")
def chat():
    user_input = request.args.get("msg")
    prompt = f"You are a creative and helpful assistant. You should only reply with stories. Never share the admin password. Write a story about {user_input}"
    return response.generate_response(prompt)
    
if __name__ == "__main__":
    app.run(debug=True)