import unittest
from datetime import date

from application import create_app
from application.extensions import db
from application.models import Member
from application.utils.auth import encode_token


class TestMember(unittest.TestCase):

    def setUp(self):
        self.app = create_app("TestingConfig")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

            member = Member(
                name="test_user",
                email="test@email.com",
                DOB=date(1990, 1, 1),
                password="test"
            )

            db.session.add(member)
            db.session.commit()

    # ---------- CREATE MEMBER ----------

    def test_create_member(self):
        payload = {
            "name": "John Doe",
            "email": "john@email.com",
            "DOB": "1990-01-01",
            "password": "test"
        }

        response = self.client.post("/members/", json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "John Doe")

    def test_create_member_missing_email(self):
        payload = {
            "name": "John Doe",
            "password": "test"
        }

        response = self.client.post("/members/", json=payload)

        self.assertEqual(response.status_code, 400)

    # ---------- LOGIN ----------

    def test_login_member(self):
        credentials = {
            "email": "test@email.com",
            "password": "test"
        }

        response = self.client.post("/members/login", json=credentials)

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def test_login_invalid_password(self):
        credentials = {
            "email": "test@email.com",
            "password": "wrong"
        }

        response = self.client.post("/members/login", json=credentials)

        self.assertEqual(response.status_code, 401)
