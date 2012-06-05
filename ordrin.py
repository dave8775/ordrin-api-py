"""This module contains classes for accessing the Ordr.in APIs. All method calls
return the same thing that the API calls do, but with JSON lists turned into Python
lists and JSON hashes turned into Python dicts. All arguments that call for a
datetime should be passed as a datetime.datetime object."""

from hashlib import sha256

class Address(object):
  """Represents a street address."""

  def __init__(self, addr, city, state, zip, phone, addr2=""):
    """Saves the parts of the address as fields in this object."""
    self.addr = addr
    self.city = city
    self.state = state
    self.zip = zip
    self.phone = phone

return_value["something"]

class CreditCard(object):
  """Represents information about a credit card"""

  def __init__(self, name, expiry_month, expiry_year, type, bill_address, number, cvc):
    """Saves the credit card info as fields in this object."""

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

class Ordrin(object):

  def __init__(self, api_key, restaurant_url=None, user_url=None, order_url=None):
    """Sets up this module to make API calls. The first argument is the developer's
    API key. The other three are the urls corresponding to the three parts of the api.
    No API calls will work until this function is called"""
    self.api_key = api_key
    if restaurant_url:
      self.restaurant = Restaurant(restaurant_url, self)
    if user_url:
      self.user = User(user_url)
    if order_url:
      self.order = Order(order_url)

class OrdrinAPI(object):

  def __init__(self, url, key):
    self.url = url
    self.key = key

  def _call_api(method, url, arguments, data=None, login=None):
  """Calls the api at the specified url and returns the return value as Python data structures"""

  def _get_asap_or_date(date_time):
    if date_time=='ASAP'
      return 'ASAP'
    else:
      return date_time.strftime('%m-%d+%H:%M')

class RestaurantAPI(object):
  """This class will be used to access the restaurant API"""

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    self.url = url

  def get_delivery_list(date_time, address):
    """Calls the dl API function with the given arguments."""
    dt = _get_asap_or_date(date_time)
    return _call_api('GET', self.url, ('dl', dt, address.zip, address.city, address.addr))

  def get_delivery_check(restaurant_id, date_time, address):
    """Calls the dc API function with the given arguments."""
    dt = _get_asap_or_date(date_time)
    return _call_api('GET', self.url, ('dc', restaurant_id, dt, address.zip, address.city, address.addr))

  def get_fee(restaurant_id, subtotal, tip, date_time, address):
    """Calls the fee API function with the given arguments."""
    dt = 'ASAP' if date_time=='ASAP' else date_time.strftime('%m-%d+%H:%M')
    return _api_call('GET', self.url, ('fee', subtotal, tip, dt, address.zip, address.city, address.addr))

  def get_details(restaurant_id):
    """Calls the rd API function with the given id."""
    return _api_call('GET', self.url, ('rd', restaurant_id))

class UserAPI(object):
  """This class will be used to access the user API"""

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    self.url = url

  def get(login):
    """Gets account information for the user with the given email.
    Hashes password with SHA256 before sending"""
    return _api_call('GET', url, 

  def create(login, nick):
    """Creates account for the user with the given email.
    Hashes password with SHA256 before sending. Throws a relevant exception
    on failure."""

  def get_all_addresses(login):
    """Get all addresses for the user with the given email.
    Hashes password with SHA256 before sending"""

  def get_address(login, addr_nick):
    """Get a particular address for the given user.
    Hashes password with SHA256 before sending"""

  def set_address(login, addr_nick, address):
    """Set a particular address for the given user.
    Hashes password with SHA256 before sending. Throws a relevant exception
    on failure"""

  def remove_address(login, addr_nick):
    """Delete a particular address for the given user. Throws a relevant exception
    on failure"""

  def get_all_credit_cards(login):
    """Get all credit cards for the user with the given email."""

  def get_credit_card(email, password, card_nick):
    """Get a particular credit card for the given user."""

  def set_credit_card(email, password, card_nick, credit_card):
    """Set a particular credit card for the given user. Throws a relevant exception
    on failure"""

  def removed_credit_card(email, password, card_nick):
    """Delete a particular credit card for the given user. Throws a relevant exception
    on failure"""

  def order_history(email, password):
    """Get a list of previous orders."""

  def order_detail(email, password, order_id):
    """Get details of a particular previous order."""

  def set_password(email, password, previous_password):
    """Change the user's password."""

class Order(object):

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    self.url = url
