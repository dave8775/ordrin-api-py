from ordrinapi import OrdrinApi
from normalize import normalize

class UserApi(OrdrinApi):
  """This class will be used to access the user API"""

  def get(self, login):
    """Gets account information for the user with the given email.
    Hashes password with SHA256 before sending"""
    return self._call_api('GET', ('u', login.email), login=login)

  def create(self, login, first_name, last_name):
    """Creates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':login.email,
            'first_name':normalize(first_name, 'name'),
            'last_name':normalize(last_name, 'name'),
            'pw':login.password}
    return self._call_api('POST', ('u', login.email), data=data)

  def update(self, login, first_name, last_name):
    """Updates account for the user with the given email. Throws a relevant exception
    on failure."""
    data = {'email':login.email,
            'first_name':normalize(first_name, 'name'),
            'last_name':normalize(last_name, 'name'),
            'pw':login.password}
    return self._call_api('POST', ('u', login.email), login=login, data=data)

  def get_all_addresses(self, login):
    """Get all addresses for the user with the given email."""
    return self._call_api('GET', ('u', login.email, 'addrs'), login=login)

  def get_address(self, login, addr_nick):
    """Get a particular address for the given user."""
    return self._call_api('GET', ('u', login.email, 'addrs', normalize(addr_nick, 'nick')), login=login)

  def set_address(self, login, addr_nick, address):
    """Set a particular address for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('PUT', ('u', login.email, 'addrs', normalize(addr_nick, 'nick')), login=login, data=address.make_dict())
      
  def remove_address(self, login, addr_nick):
    """Delete a particular address for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('DELETE', ('u', login.email, 'addrs', normalize(addr_nick, 'nick')), login=login)

  def get_all_credit_cards(self, login):
    """Get all credit cards for the user with the given email."""
    return self._call_api('GET', ('u', login.email, 'ccs'), login=login)

  def get_credit_card(self, login, card_nick):
    """Get a particular credit card for the given user."""
    return self._call_api('GET', ('u', login.email, 'ccs', normalize(card_nick, 'nick')), login=login)

  def set_credit_card(self, login, card_nick, credit_card, phone):
    """Set a particular credit card for the given user. Throws a relevant exception
    on failure"""
    card_nick = normalize(card_nick, 'nick')
    data = credit_card.make_dict()
    data.update(login.make_dict())
    data['nick'] = card_nick
    data['phone'] = normalize(phone, 'phone')
    return self._call_api('PUT', ('u', login.email, 'ccs', card_nick), login=login, data=data)

  def remove_credit_card(self, login, card_nick):
    """Delete a particular credit card for the given user. Throws a relevant exception
    on failure"""
    return self._call_api('DELETE', ('u', login.email, 'ccs', normalize(card_nick, 'nick')), login=login)

  def get_order_history(self, login):
    """Get a list of previous orders."""
    return self._call_api('GET', ('u', login.email, 'orders'), login=login)

  def get_order_detail(self, login, order_id):
    """Get details of a particular previous order."""
    return self._call_api('GET', ('u', login.email, 'orders', normalize(order_id, 'number')), login=login)

  def set_password(self, login, new_password):
    """Change the user's password."""
    data = {'email': login.email,
            'password': UserLogin.hash_password(new_password),
            'previous_password': login.password}
    return self._call_api('PUT', ('u', login.email, 'password'), login=login, data=data)
