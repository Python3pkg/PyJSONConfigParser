# -*- coding: utf-8 -*-

import unittest

import datetime

import pytz

import JSONConfigParser

class TestConfigParser(unittest.TestCase):
  def setUp(self):
    pass

  def test_dumps_datetime(self):
    tm = datetime.datetime(year=2015, month=1, day=1, hour=0, minute=0, second=0)
    r = JSONConfigParser.dumps(tm)
    self.assertEqual(r, '{"__datetime.datetime__": "2015-01-01T00:00:00+00:00"}')

    tm = datetime.datetime(year=2015, month=1, day=1, hour=0, minute=0, second=0, tzinfo=pytz.utc)
    r = JSONConfigParser.dumps(tm)
    self.assertEqual(r, '{"__datetime.datetime__": "2015-01-01T00:00:00+00:00"}')

    tm = datetime.datetime(year=2015, month=1, day=1, hour=9, minute=0, second=0, tzinfo=pytz.timezone('Asia/Tokyo'))
    r = JSONConfigParser.dumps(tm)
    self.assertEqual(r, '{"__datetime.datetime__": "2015-01-01T00:00:00+00:00"}')

  def test_loads_datetime(self):
    tm_txt = '{"__datetime.datetime__": "2015-01-01T00:00:00+00:00"}'
    tm = datetime.datetime(year=2015, month=1, day=1, hour=0, minute=0, second=0, tzinfo=pytz.utc)
    r = JSONConfigParser.loads(tm_txt)
    self.assertEqual(r, tm)


def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestConfigParser))
  return suite
