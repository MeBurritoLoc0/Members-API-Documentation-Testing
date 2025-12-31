from flask import Blueprint, request, jsonify

math_bp = Blueprint("math", __name__, url_prefix="/math")

@math_bp.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    return jsonify({"result": data["num1"] + data["num2"]})

@math_bp.route("/subtract", methods=["POST"])
def subtract_numbers():
    data = request.get_json()
    return jsonify({"result": data["num1"] - data["num2"]})

@math_bp.route("/multiply", methods=["POST"])
def multiply_numbers():
    data = request.get_json()
    return jsonify({"result": data["num1"] * data["num2"]})

@math_bp.route("/divide", methods=["POST"])
def divide_numbers():
    data = request.get_json()
    return jsonify({"result": data["num1"] / data["num2"]})
