from flask import Flask, render_template, session, redirect


app = Flask(__name__)
app.secret_key = 'MyScretKey'


@app.route("/")
def root():
    if ("views" in session):
        session["views"] += 1
    else:
        session["views"] = 0
    return render_template('index.html')


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
