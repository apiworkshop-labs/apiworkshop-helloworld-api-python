import unittest
import subprocess
import time
import os
import signal
import http.client

class TestHelloWorldEndpoints(unittest.TestCase):
    PORT = 8000

    @classmethod
    def setUpClass(cls):
        cls.process = subprocess.Popen(["python", "src/app.py"])
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        os.kill(cls.process.pid, signal.SIGTERM)

    def test_without_name(self):
        conn = http.client.HTTPConnection("localhost", self.PORT)
        conn.request("GET", "/")
        response = conn.getresponse()
        body = response.read().decode()
        self.assertEqual(response.status, 200)
        self.assertEqual(body, "Hello, World!")
        conn.close()

    def test_with_name(self):
        conn = http.client.HTTPConnection("localhost", self.PORT)
        conn.request("GET", "/?name=Alice")
        response = conn.getresponse()
        body = response.read().decode()
        self.assertEqual(response.status, 200)
        self.assertEqual(body, "Hi Alice,\nHow are you?")
        conn.close()

if __name__ == "__main__":
    unittest.main()
