from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

sia = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def home():

    user_message = ""
    bot_response = ""
    sentiment = ""

    if request.method == "POST":

        user_message = request.form["message"]

        score = sia.polarity_scores(user_message)

        compound = score['compound']

        if compound >= 0.05:
            sentiment = "Positive 😊"
            bot_response = "I'm glad you're feeling good!"

        elif compound <= -0.05:
            sentiment = "Negative 😟"
            bot_response = "I'm sorry you're upset. Tell me more."

        else:
            sentiment = "Neutral 😐"
            bot_response = "I understand. How can I help you further?"

    return render_template(
        "index.html",
        user_message=user_message,
        bot_response=bot_response,
        sentiment=sentiment
    )

if __name__ == "__main__":
    app.run(debug=True)