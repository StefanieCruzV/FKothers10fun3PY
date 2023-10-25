from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("youre axcesin to index routes!")
    return "hey its me the main page "

@app.route("/second")
def second():
    print("youre axcesin to index routes!")
    return "this is the second"

@app.route("/repeat/<phrase>")
def repeat_phrase(phrase):
    return f"your phrase is: {phrase}"

@app.route("/repeat/<phrase>/<int:times>")
def repeat_times(phrase,times):
    repeated = phrase * times
    return repeated

@app.route("/main") 
def main():
    print("return html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
