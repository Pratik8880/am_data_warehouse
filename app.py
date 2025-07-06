from flask import Flask
from models import db
from routes.normalized_routes import normalized_bp
from routes.merged_routes import merged_bp

app = Flask(__name__)         #Create a flask app instance 
app.config.from_pyfile('config.py')
db.init_app(app)

# Register Blueprints (route groups)
app.register_blueprint(normalized_bp)
app.register_blueprint(merged_bp)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return "✅ Flask API is running!"

