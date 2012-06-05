import ordrin
class UserAPI(ordrin.OrdrinAPI):
  """This class will be used to access the user API"""

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    ordrin.OrdrinAPI.__init__(self, url)

  def get(login):
    """Gets account information for the user with the given email.
    Hashes password with SHA256 before sending"""
    return self._call_api('GET', ('u', login.email), login=login)

  def create(login, first_name, last_name):
    """Creates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':email, 'first_name':first_name, 'last_name':last_name, 'pw':login.passhash}
    return self._call_api('POST', ('u', login.email), data=data)

  def update(login, nick, first_name, last_name):
    """Updates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':email, 'first_name':first_name, 'last_name':last_name, 'pw':login.passhash}
    return self._call_api('POST', ('u', login.email), login=login, data=data)

  def get_all_addresses(login):
    """Get all addresses for the user with the given email."""
    return self._call_api('GET', ('u', login.email, 'addrs'), login=login)

  def get_address(login, addr_nick):
    """Get a particular address for the given user."""
    return self._call_api('GET', ('u', login.email, 'addrs', addr_nick), login=login)

  def set_address(login, addr_nick, address):
    """Set a particular address for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('POST', ('u', login.email, 'addrs', addr_nick), login=login, data=address.make_dict())
      
  def remove_address(login, addr_nick):
    """Delete a particular address for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('DELETE', ('u', login.email, 'addrs', addr_nick), login=login)

  def get_all_credit_cards(login):
    """Get all credit cards for the user with the given email."""
    return self._call_api('GET', ('u', login.email, 'ccs'), login=login)

  def get_credit_card(email, password, card_nick):
    """Get a particular credit card for the given user."""
    return self._call_api('GET', ('u', login.email, 'ccs', card_nick), login=login)

  def set_credit_card(email, password, card_nick, credit_card):
    """Set a particular credit card for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('PUT', ('u', login.email, 'ccs', card_nick), login=login, data=credit_card.make_dict())

  def remove_credit_card(email, password, card_nick):
    """Delete a particular credit card for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('DELETE', ('u', login.email, 'ccs', card_nick), login=login)

  def get_order_history(login):
    """Get a list of previous orders."""
    return self._call_api('GET', ('u', login.email, 'orders'), login=login)

  def get_order_detail(email, password, order_id):
    """Get details of a particular previous order."""
    return self._call_api('GET', ('u', login.email, 'orders', order_id), login=login)

  def set_password(login, new_password):
    """Change the user's password."""
    return self._call_api('PUT', ('u', login.email, 'password'), login=login, data={'password':new_password})
