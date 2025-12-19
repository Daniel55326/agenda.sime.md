import os
from flask import Flask, send_from_directory, request
import datetime

app = Flask(__name__, static_folder=".", static_url_path="")

# 🟦 LOG Vizitatori (IP + Device)
def log_user():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.user_agent.string
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("visitors.log", "a") as f:
        f.write(f"[{time}] IP: {ip} | DEVICE: {user_agent}\n")

# 🟦 Home
@app.route("/")
def index():
    log_user()
    return send_from_directory(".", "index.html")

# 🟦 Orice alt fișier (html, css, js, imagini)
@app.route("/<path:path>")
def static_files(path):
    log_user()
    return send_from_directory(".", path)

# 🟦 Pornire LOCAL / Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
