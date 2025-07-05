from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)  # <-- THIS is what gunicorn is looking for

api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

@app.route("/", methods=["GET"])
def home():
    return "Genbot is live!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
