from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Azure App Service!</h1>
    <h2>My Flask App is Working.</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)