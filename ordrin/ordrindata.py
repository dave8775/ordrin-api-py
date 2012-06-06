"""This module contains all of the data structures that the ordrin package uses
to pass around non-builtin groups of data"""

import inspect

def _validate(value, regex, err_msg):
  try:
    return re.match(regex, value).group(0)
  except AttributeError:
    raise ValueError(err_msg) 

class OrdrinData(object):
  """Base class for objects that can save any data with the constructor and then
  extract it as a dictionary"""

  def __init__(self, **kwargs):
    for k in kwargs:
      self.__setattr__(k, kwargs[k])

  def make_dict(self):
    return {f:self.__getattribute__(f) for f in self.fields}

class Address(OrdrinData):
  """Represents a street address."""

  fields = ('addr', 'city', 'state', 'zip', 'phone')

  def __init__(self, addr, city, state, zip, phone, addr2="", **kwargs):
    """Store the parts of the address as fields in this object. Any additional keyword arguments
    will be discarded."""
    _validate(state, r'^[A-Z]{2}$', "state must be a standard two letter postal code abbreviation")
    _validate(zip, r'^\d{5}(-\d{4})?$', "zip must be a 5 digit zip code with an optional 4 digit add-on code")
    _validate(phone, r'^\d{3}-\d{3}-\d{4}$', "phone must be of the form '###-###-####' where # is a digit")
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
    _validate(str(expiry_month), r'^\d{2}$', "expiry_month must be two digits")
    _validate(str(expiry_year), r'^\d{4}$', "expiry_yaer must be four digits")
    _validate(str(cvc), r'^\d{3,4}$', "cvc must be a 3 or 4 digit security code")
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
    self.email = email
    self.password = UserLogin.hash_password(password)

  @classmethod
  def hash_password(cls, password):
    return sha256(password).hexdigest()

class TrayItem(object):
  """Represents a single item in an order"""
  
  def __init__(self, item_id, quantity, *options):
    """Store the descriptors of an order item in this object."""
    _validate(str(item_id), r'^\d+$', "item_id must be a natural number")
    _validate(str(quantity), r'^\d+$', "quantity must be a positive natural number")
    all(_validate(str(option), r'^\d+$', "all options must be natural numbers") for option in options)
    self.id = item_id
    self.quantity = quantity
    self.options = options

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
