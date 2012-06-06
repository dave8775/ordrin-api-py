"""This module contains all of the data structures that the ordrin package uses
to pass around non-builtin groups of data"""

import inspect
from hashlib import sha256

from normalize import normalize

class OrdrinData(object):
  """Base class for objects that can save any data with the constructor and then
  extract it as a dictionary"""

  def __init__(self, **kwargs):
    for k in kwargs:
      setattr(self, k, kwargs[k])

  def make_dict(self):
    return {f:getattr(self, f) for f in self.fields}

class Address(OrdrinData):
  """Represents a street address."""

  fields = ('addr', 'city', 'state', 'zip', 'phone')

  def __init__(self, addr, city, state, zip, phone, addr2="", **kwargs):
    """Store the parts of the address as fields in this object. Any additional keyword arguments
    will be discarded."""
    state = normalize(state, 'state')
    zip = normalize(zip, 'zip')
    phone = normalize(phone, 'phone')
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    OrdrinData.__init__(self, **{k:values[k] for k in args if k!='self'})

class CreditCard(OrdrinData):
  """Represents information about a credit card"""

  fields = ('number', 'cvc', 'expiry_month', 'expiry_year', 'expiry',
            'bill_addr', 'bill_addr2', 'bill_city', 'bill_state', 'bill_zip')

  def __init__(self, name, expiry_month, expiry_year, type, bill_address, number, cvc, **kwargs):
    """Store the credit card info as fields in this object. Any additional keyword arguments
    will be discarded"""
    expiry_month = normalize(expiry_month, 'month')
    expiry_year = normalize(expiry_year, 'year')
    cvc = normalize(cvc, 'cvc')
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    OrdrinData.__init__(self, **{k:values[k] for k in args})

  @property
  def bill_addr(self):
    return self.bill_address.addr

  @property
  def bill_addr2(self):
    return self.bill_address.addr2

  @property
  def bill_city(self):
    return self.bill_address.city

  @property
  def bill_state(self):
    return self.bill_address.state

  @property
  def bill_zip(self):
    return self.bill_address.zip

  @property
  def expiry(self):
    """A combination of the expiry_month and expiry_date"""
    return '{}/{}'.format(self.expiry_month, self.expiry_year)

class UserLogin(OrdrinData):

  fields = ('email', 'password')

  def __init__(self, email, password):
    """Store the email and password in this object. Saves only the hash of the
    password, not the password itself"""
    self.email = normalize(email, 'email')
    self.password = UserLogin.hash_password(password)

  @classmethod
  def hash_password(cls, password):
    return sha256(password).hexdigest()

class TrayItem(object):
  """Represents a single item in an order"""
  
  def __init__(self, item_id, quantity, *options):
    """Store the descriptors of an order item in this object."""
    self.item_id = normalize(item_id, number)
    self.quantity = normalize(quantity, number)
    self.options = [normalize(option, number) for option in options]

  def __str__(self):
    return '{}/{},{}'.format(self.id, self.quantity, ','.join(str(opt) for opt in options))

class Tray(object):
  """Represents a list of items in an order"""

  def __init__(self, *items):
    """Store the list of items in this object. Each argument should be of type
    Item"""
    self.items = items

  def __str__(self):
    return '+'.join(str(i) for i in items)
