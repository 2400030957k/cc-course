from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CC Course Project</title>
        </head>
        <body>
            <h1>CC Course Project</h1>
            <p>Azure Web App is running successfully!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
