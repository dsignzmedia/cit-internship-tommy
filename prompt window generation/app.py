from flask import Flask, render_template, request, send_file, jsonify
from generator import chatbot_response
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # ✅ Intro page

@app.route("/generator")
def generator_page():
    return render_template("generator.html")  # ✅ Your second page

@app.route("/generate", methods=["POST"])
def generate():
    user_text = request.form["design"]
    image, _ = chatbot_response(user_text)

    if image:
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        base64_image = base64.b64encode(buffer.read()).decode('utf-8')
        return jsonify({"image": base64_image})
    else:
        return jsonify({"error": "❌ Could not generate design"}), 400

if __name__ == "__main__":
    app.run(debug=True)
