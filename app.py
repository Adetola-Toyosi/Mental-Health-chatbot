from flask import Flask, render_template, request
import chatbot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/get")
def get_bot_response():
    user_response = request.args.get('msg')
    return str(chatbot.chat_response(user_response))


if __name__ == "__main__":
    app.run(debug=True)
