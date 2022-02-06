try:
    import unittest
    from server import app
    import json
    
except Exception as e:
    print('Some modules are missing {} '.format(e))

class APITest(unittest.TestCase):
    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/Ping')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == '__main__':
    unittest.main()