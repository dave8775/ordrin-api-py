from hashlib import sha256
import requests
import inspect

class OrdrinData(object):

  def __init__(self, **kwargs):
    for k in kwargs:
      self.__setattr__(k, kwargs[k])

  def make_dict(self):
    return {f:self.__getattribute__(f) for f in self.fields}

class Address(OrdrinData):
  """Represents a street address."""

  fields = ('addr', 'city', 'state', 'zip', 'phone')

  def __init__(self, addr, city, state, zip, phone, addr2=""):
    """Saves the parts of the address as fields in this object."""
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    OrdrinData.__init__(self, {k:values[k] for k in args})

class CreditCard(OrdrinData):
  """Represents information about a credit card"""

  def __init__(self, name, expiry_month, expiry_year, type, bill_address, number, cvc):
    """Saves the credit card info as fields in this object."""
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    OrdrinData.__init__(self, {k:values[k] for k in args})
##    self.name = name
##    self.expiry_month = expiry_month
##    self.expiry_year = expiry_year
##    self.type = type
##    self.bill_address = bill_address
##    self.number = number
##    self.cvc = cvc

  @property
  def bill_addr(self):
    return bill_address.addr

  @property
  def bill_addr2(self):
    return bill_address.addr2

  @property
  def bill_city(self):
    return bill_address.city

  @property
  def bill_state(self):
    return bill_address.state

  @property
  def bill_zip(self):
    return bill_address.zip

class UserLogin(object):

  def __init__(self, email, password):
    self.email = email
    self.passhash = sha256(password).hexdigest()

class TrayItem(object):
  def __init__(self, item_id, quantity, *options):
    self.id = item_id
    self.quantity = quantity
    self.options = options

  def __str__(self):
    return '{}/{},{}'.format(self.id, self.quantity, ','.join(str(opt) for opt in options))

class Tray(object):

  def __init__(self, *items):
    self.items = items

  def __str__(self):
    return ','.join(str(i) for i in items)

class OrdrinException(Exception):
  pass

class OrdrinAPI(object):

  def __init__(self, url, key):
    self.url = url
    self.key = key

  def _call_api(method, arguments, login=None, data=None):
    """Calls the api at the specified url and returns the return value as Python data structures.
    Rethrows any api error as a Python exception"""

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
