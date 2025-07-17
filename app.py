
from flask import Flask
from routes.voice_routes import voice_bp
from routes.text_routes import text_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(voice_bp)
app.register_blueprint(text_bp)

@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port,debug=True)
