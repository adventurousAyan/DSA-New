import re
from deploy_helper import DeployHelper
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/api/deploy", methods=["POST"])
def deploy_model():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        model_data = request.json
        helper = DeployHelper(model_data)
        res = helper.deploy_model()
        return res.toJson()


if __name__ == "__main__":
    app.run()
