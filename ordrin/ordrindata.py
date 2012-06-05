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
    OrdrinData.__init__(self, **{k:values[k] for k in args})

class CreditCard(OrdrinData):
  """Represents information about a credit card"""

  fields = ('number', 'cvc', 'expiry_month', 'expiry_year', 'expiry',
            'bill_addr', 'bill_addr2', 'bill_city', 'bill_state', 'bill_zip')

  def __init__(self, name, expiry_month, expiry_year, type, bill_address, number, cvc):
    """Saves the credit card info as fields in this object."""
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
    return '{}/{}'.format(self.expiry_month, self.expiry_year)

class UserLogin(OrdrinData):

  fields = ('email', 'password')

  def __init__(self, email, password):
    self.email = email
    self.password = UserLogin.encrypt_password(password)

  @classmethod
  def encrypt_password(cls, password):
    return sha256(password).hexdigest()

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
    return '+'.join(str(i) for i in items)
