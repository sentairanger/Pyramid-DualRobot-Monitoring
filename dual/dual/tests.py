import unittest
from pyramid import testing

class DualFunctionalTests(unittest.TestCase):
    def setUp(self):
        from dual import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)
    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'', res.body)
    def test_css(self):
        res = self.testapp.get('/static/dual.css', status=200)
        self.assertIn(b'body', res.body)
    def test_js(self):
        res = self.testapp.get('/static/dual.js', status=200)
        self.assertIn(b'body', res.body)
    def test_forward(self):
        res = self.testapp.get('/forward', status=200)
        self.assertIn(b'', res.body)
    def test_backward(self):
        res = self.testapp.get('/backward', status=200)
        self.assertIn(b'', res.body)
    def test_left(self):
        res = self.testapp.get('/left', status=200)
        self.assertIn(b'', res.body)
    def test_right(self):
        res = self.testapp.get('/right', status=200)
        self.assertIn(b'', res.body)
    def test_stop(self):
        res = self.testapp.get('/stop', status=200)
        self.assertIn(b'', res.body)
    def test_north(self):
        res = self.testapp.get('/north', status=200)
        self.assertIn(b'', res.body)
        
    def test_south(self):
        res = self.testapp.get('/south', status=200)
        self.assertIn(b'', res.body)
    def test_west(self):
        res = self.testapp.get('/west', status=200)
        self.assertIn(b'', res.body)
    def test_east(self):
        res = self.testapp.get('/east', status=200)
        self.assertIn(b'', res.body)
    def test_stoptwo(self):
        res = self.testapp.get('/stoptwo', status=200)
        self.assertIn(b'', res.body)
    def test_torvaldson(self):
        res = self.testapp.get('/torvaldson', status=200)
        self.assertIn(b'', res.body)
    def test_torvaldsoff(self):
        res = self.testapp.get('/torvaldsoff', status=200)
        self.assertIn(b'', res.body)
    def test_linuseye(self):
        res = self.testapp.get('/linuson', status=200)
        self.assertIn(b'', res.body)
    def test_linusoff(self):
        res = self.testapp.get('/linusoff', status=200)
        self.assertIn(b'', res.body)
    def test_servomin(self):
        res = self.testapp.get('/servomin', status=200)
        self.assertIn(b'', res.body)
        
    def test_servomid(self):
        res = self.testapp.get('/servomid', status=200)
        self.assertIn(b'', res.body)
    def test_servomax(self):
        res = self.testapp.get('/servomax', status=200)
        self.assertIn(b'', res.body)
    def test_servomin2(self):
        res = self.testapp.get('/servomin2', status=200)
        self.assertIn(b'', res.body)
        
    def test_servomid2(self):
        res = self.testapp.get('/servomid2', status=200)
        self.assertIn(b'', res.body)
    def test_servomax2(self):
        res = self.testapp.get('/servomax2', status=200)
        self.assertIn(b'', res.body)
    def test_thirty(self):
        res = self.testapp.get('/thirty', status=200)
        self.assertIn(b'', res.body)
    def test_fifty(self):
        res = self.testapp.get('/fifty', status=200)
        self.assertIn(b'', res.body)
    def test_full(self):
        res = self.testapp.get('/full', status=200)
        self.assertIn(b'', res.body)