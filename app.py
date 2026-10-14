
from flask import Flask, request
import secrets
import string

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        try:
            length = int(request.form["length"])

            if not 8 <= length <= 64:
                password = "Choose a length between 8 and 64."
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = "".join(
                    secrets.choice(characters) for _ in range(length)
                )
        except ValueError:
            password = "Enter a valid password length."

    return f"""
    <html>
    <head>
        <title>Password Generator</title>
    </head>
    <body>
        <h1>Password Generator</h1>

        <form method="post">
            <label>Password length (8-64):</label>
            <input type="number" name="length"
                   min="8" max="64" value="12" required>
            <button type="submit">Generate Password</button>
        </form>

        <h3>Your Password:</h3>
        <p>{password}</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
