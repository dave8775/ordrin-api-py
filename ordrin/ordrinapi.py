from hashlib import sha256
import requests
import json
import re
import urllib
from ordrindata import _validate

class OrdrinError(Exception):
  pass

class OrdrinAPI(object):
  """A base object for calling one part of the ordr.in API"""

  def __init__(self, key, base_url):
    """Save the url and key parameters in the object"""
    self.base_url = _validate(base_url, r'(https?://)?[-\w.~]+(/+[-\w.~]+)*', "base_url must be a valid URL")+'/'
    #As far as I can tell, there is no good test for an invalid key
    self.key = key

  def _call_api(self, method, arguments, login=None, data=None):
    """Calls the api at the saved url and returns the return value as Python data structures.
    Rethrows any api error as a Python exception"""
    methods = {'GET':requests.get, 'POST':requests.post, 'PUT':requests.put, 'DELETE':requests.delete}
    full_url = self.base_url+'/'.join(urllib.quote_plus(str(arg)) for arg in arguments)
    #for debugging purposes only
    print "requesting from:", full_url
    headers = {'X-NAAMA-CLIENT-AUTHENTICATION': 'id="{}", version="1"'.format(self.key)}
    if login:
      hash_code = sha256(login.password, login.email, full_url).hex_digest()
      headers['X-NAAMA-AUTHENTICATION'] = 'username="{}", response="{}", version="1"'.format(login.email, hash_code)
    r = methods[method](full_url, data=data)
    r.raise_for_status()
    result = json.loads(r.text)
    if '_error' in result and result['_error']:
      if 'text' in result:
        raise OrdrinError((result['msg'], result['text']))
      else:
        raise OrdrinError(result['msg'])
    return result

  def _get_asap_or_datetime(self, date_time):
    if date_time=='ASAP':
      return 'ASAP'
    else:
      try:
        return date_time.strftime('%m-%d+%H:%M')
      except AttributeError:
        raise TypeError("date_time must be a datetime.datetime object or the string 'ASAP'")

  def _get_asap_or_date(self, date_time):
    if date_time=='ASAP':
      return ASAP
    else:
      try:
        return date_time.strftime('%m-%d')
      except AttributeError:
        raise TypeError("date_time must be a datetime.datetime or datetime.date object or the string 'ASAP'")
