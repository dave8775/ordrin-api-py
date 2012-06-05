from ordrinapi import OrdrinAPI

class UserAPI(OrdrinAPI):
  """This class will be used to access the user API"""

  def get(login):
    """Gets account information for the user with the given email.
    Hashes password with SHA256 before sending"""
    return self._call_api('GET', ('u', login.email), login=login)

  def create(login, first_name, last_name):
    """Creates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':login.email, 'first_name':first_name, 'last_name':last_name, 'pw':login.password}
    return self._call_api('POST', ('u', login.email), data=data)

  def update(login, nick, first_name, last_name):
    """Updates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':login.email, 'first_name':first_name, 'last_name':last_name, 'pw':login.password}
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

  def get_credit_card(login, card_nick):
    """Get a particular credit card for the given user."""
    return self._call_api('GET', ('u', login.email, 'ccs', card_nick), login=login)

  def set_credit_card(login, card_nick, credit_card, phone):
    """Set a particular credit card for the given user. Throws a relevant exception
    on failure"""
    data = credit_card.make_dict()
    data.update(login.make_dict())
    data['nick'] = card_nick
    data['phone'] = phone
    return self._call_api('PUT', ('u', login.email, 'ccs', card_nick), login=login, data=credit_card.make_dict())

  def remove_credit_card(login, card_nick):
    """Delete a particular credit card for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('DELETE', ('u', login.email, 'ccs', card_nick), login=login)

  def get_order_history(login):
    """Get a list of previous orders."""
    return self._call_api('GET', ('u', login.email, 'orders'), login=login)

  def get_order_detail(login, order_id):
    """Get details of a particular previous order."""
    return self._call_api('GET', ('u', login.email, 'orders', order_id), login=login)

  def set_password(login, new_password):
    """Change the user's password."""
    return self._call_api('PUT', ('u', login.email, 'password'), login=login, data={'password':new_password})
