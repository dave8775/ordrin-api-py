from hashlib import sha256
import requests
import json
import re
import urllib

class OrdrinError(Exception):
  pass

class OrdrinAPI(object):
  """A base object for calling one part of the ordr.in API"""

  def __init__(self, base_url, key):
    """Save the url and key parameters in the object"""
    try:
      self.base_url = re.match(r'(https?://)?[-\w.~]+(/+[-\w.~]+)*', base_url).group(0) + '/'
    except AttributeError:
      raise ValueError("base_url must be a valid URL")
    self.key = key

  def _call_api(method, arguments, login=None, data=None):
    """Calls the api at the saved url and returns the return value as Python data structures.
    Rethrows any api error as a Python exception"""
    methods = {'GET':requests.get, 'POST':requests.post, 'PUT':requests.put, 'DELETE':requests.delete}
    full_url = self.base_url+'/'.join(urllib.quote_plus(str(arg)) for arg in arguments)
    headers = {'X-NAAMA-CLIENT-AUTHENTICATION': 'id="{}", version="1"'.format(self.key)}
    if login:
      hash_code = sha256(login.password, login.email, full_url).hex_digest()
      headers['X-NAAMA-AUTHENTICATION'] = 'username="{}", response="{}", version="1"'.format(login.email, hash_code)
    r = methods[method](full_url, data=data)
    r.raise_for_status()
    result = json.load(r.text)
    if '_error' in result and result['_error']:
      if 'text' in result:
        raise OrdrinError((result['msg'], result['text']))
      else:
        raise OrdrinError(result['msg'])
    return result

  def _get_asap_or_datetime(date_time):
    if date_time=='ASAP':
      return 'ASAP'
    else:
      return date_time.strftime('%m-%d+%H:%M')

  def _get_asap_or_date(date_time):
    if date_time=='ASAP':
      return ASAP
    else:
      return date_time.strftime('%m-%d')
