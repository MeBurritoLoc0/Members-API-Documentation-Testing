import unittest
from app import create_app


class TestMathAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def test_sum(self):
        payload = {"num1": 2, "num2": 3}
        response = self.client.post("/math/sum", json=payload)
        data = response.get_json()
        self.assertEqual(data["result"], 5)

    def test_subtract(self):
        payload = {"num1": 10, "num2": 4}
        response = self.client.post("/math/sum", json=payload)
        data = response.get_json()
        self.assertEqual(data["result"], 6)

    def test_multiply(self):
        payload = {"num1": 6, "num2": 7}
        response = self.client.post("/math/sum", json=payload)
        data = response.get_json()
        self.assertEqual(data["result"], 42)

    def test_divide(self):
        payload = {"num1": 8, "num2": 2}
        response = self.client.post("/math/sum", json=payload)
        data = response.get_json()
        self.assertEqual(data["result"], 4)


if __name__ == "__main__":
    unittest.main()
