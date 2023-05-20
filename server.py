from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def show_page():
    return render_template("index.html")


def main():
    app.run()


if __name__ == '__main__':
    main()
