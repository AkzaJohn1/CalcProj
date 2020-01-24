from flask import Flask, request,Blueprint
from scripts.services import request_calc
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(request_calc.calculator_service)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5002")
