from flask import Blueprint, request, jsonify
from datetime import datetime

from application.models import Member
from application.extensions import db
from application.utils.auth import encode_token


# ✅ DEFINE THE BLUEPRINT
members_bp = Blueprint("members", __name__, url_prefix="/members")


# ---------- CREATE MEMBER ----------
@members_bp.route("/", methods=["POST"])
def create_member():
    data = request.get_json()

    required = ["name", "email", "DOB", "password"]
    for field in required:
        if field not in data:
            return jsonify({field: ["Missing data for required field."]}), 400

    member = Member(
    name=data["name"],
    email=data["email"],
    DOB=datetime.strptime(data["DOB"], "%Y-%m-%d").date(),
    password=data["password"]
)


    db.session.add(member)
    db.session.commit()

    return jsonify({
        "name": member.name,
        "email": member.email,
        "DOB": str(member.DOB)
    }), 201


# ---------- LOGIN MEMBER ----------
@members_bp.route("/login", methods=["POST"])
def login_member():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"message": "Missing credentials"}), 400

    member = Member.query.filter_by(email=data["email"]).first()

    if not member or member.password != data["password"]:
        return jsonify({"message": "Invalid credentials"}), 401

    token = encode_token(member.id)

    return jsonify({
        "status": "success",
        "token": token
    }), 200

