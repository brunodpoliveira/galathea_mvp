from flask import Flask, render_template, request
from chatbot import bot


# --------------------------------------

# GUI + website
app = Flask(__name__)
ENV = 'dev'

# --------------------------------------


@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(bot.get_response(usertext))

# --------------------------------------


if __name__ == "__main__":
    app.run()
# --------------------------------------
