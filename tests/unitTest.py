#!/usr/bin/env python
import unittest
import sys
sys.path.insert(1, '/app/src')
import app


class TestService(unittest.TestCase):
  def setUp(self):
    app.app.testing = True
    self.app = app.app.test_client()

  def test_service(self):
    rv = self.app.get('/')
    self.assertEqual(rv.status, '200 OK')

  def test_stats(self):
    rv = self.app.get('/stats')
    self.assertEqual(rv.status, '200 OK')

  def test_api(self):
    rv = self.app.get('/api')
    self.assertEqual(rv.status, '200 OK')

  def test_health(self):
    rv = self.app.get('/health')
    self.assertEqual(rv.status, '200 OK')
    self.assertEqual(rv.data, b'OK')

if __name__ == '__main__':
  unittest.main()
