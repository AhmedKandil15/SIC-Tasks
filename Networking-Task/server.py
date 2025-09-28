from flask import Flask, jsonify, request

app = Flask(__name__)

temperature = 25


@app.get("/temp")
def get_temp():
    return jsonify({"temperature": temperature})


@app.post("/temp")
def update_temp():
    global temperature
    data = request.get_json()
    temperature = int(data["temperature"])
    return jsonify({"temperature": temperature})


if __name__ == "__main__":
    app.run()
