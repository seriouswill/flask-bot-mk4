from flask import Flask, render_template, request
from chatbot import predict_class, get_response, intents


app = Flask(__name__)

app.config['SECRET__KEY'] = 'a_very_secretive_key_123456789'

answer_list = []


@app.route("/")
def home():
    global answer_list
    answer_list.clear()
    return render_template("index.html")


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    global answer_list

    if request.method == "POST":

        message = request.form['message']
        ints = predict_class(message)
        res = get_response(ints, intents)
        answer_list.append(res)
        print(answer_list)
        if len(answer_list) > 5:
            answer_list.remove(answer_list[0])

        return render_template("chatbot.html", message=message, res=res, answer_list=answer_list)

    return render_template("chatbot.html", message="", answer_list=answer_list)


if __name__ == "__main__":
    app.run(debug=False)
