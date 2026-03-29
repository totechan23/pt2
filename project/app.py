from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

complaints = []
sos_list = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/citizen")
def citizen():
    return render_template("citizen.html")

@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    text = data["message"].lower()

    # SOS
    if "unsafe" in text or "help" in text:
        sos_list.append(text)
        return jsonify({"response": "🚨 SOS Triggered!"})

    # Complaint
    elif "water" in text or "light" in text:
        complaints.append({"text": text, "status": "Pending"})
        return jsonify({"response": "✅ Complaint Registered!"})

    # Query
    else:
        return jsonify({"response": "💬 Query received!"})

@app.route("/data")
def get_data():
    return jsonify({
        "complaints": complaints,
        "sos": sos_list
    })

if __name__ == "__main__":
    app.run(debug=True)