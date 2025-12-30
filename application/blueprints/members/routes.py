from flask import Blueprint, request, jsonify

# Create blueprint (NO url_prefix — tests expect root paths)
math_bp = Blueprint("math", __name__)


@math_bp.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    result = data["num1"] + data["num2"]
    return jsonify({"result": result})


@math_bp.route("/subtract", methods=["POST"])
def subtract_numbers():
    data = request.get_json()
    result = data["num1"] - data["num2"]
    return jsonify({"result": result})


@math_bp.route("/multiply", methods=["POST"])
def multiply_numbers():
    data = request.get_json()
    result = data["num1"] * data["num2"]
    return jsonify({"result": result})


@math_bp.route("/divide", methods=["POST"])
def divide_numbers():
    data = request.get_json()
    result = data["num1"] / data["num2"]
    return jsonify({"result": result})

