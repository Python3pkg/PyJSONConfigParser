# -*- coding: utf-8 -*-

import json
import datetime

import pytz

__version__ = '0.0.1'
__all__ = [
    'dumps', 'loads',
]

__author__ = 'KAWASAKI Yasukazu <kawasaki@dev.kawa1128.jp>'

class _NNE4FineJsonEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      if obj.tzinfo is None:
        obj = obj.replace(tzinfo=pytz.utc)
      else:
        obj = obj.astimezone(pytz.utc)
      obj.replace(microsecond=0)
      return {'__datetime.datetime__': obj.isoformat()}
    return json.JSONEncoder.default(self, obj)

def _NNE4FineJsonDecoder_hook(dct):
  if '__datetime.datetime__' in dct:
    tm_str = dct['__datetime.datetime__']
    if tm_str.endswith('+00:00'):
      # 2015-01-01T00:00:00+00:00
      tm = datetime.datetime.strptime(tm_str, '%Y-%m-%dT%H:%M:%S+00:00')
      tm = tm.replace(tzinfo=pytz.utc)
      return tm
  return dct

def dumps(obj):
  return json.dumps(obj, cls=_NNE4FineJsonEncoder)

def loads(s):
  if not isinstance(s, str):
    raise TypeError('ConfigFile Object is not str, not {!r}'.format(s.__class__.__name__))
  return json.loads(s, object_hook=_NNE4FineJsonDecoder_hook)
