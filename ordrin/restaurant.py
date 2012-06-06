from ordrinapi import OrdrinAPI
from normalize import normalize

class RestaurantAPI(OrdrinAPI):
  """This class will be used to access the restaurant API"""

  def get_delivery_list(self, date_time, address):
    """Call the dl API function with the given arguments."""
    dt = normalize(date_time, 'datetime')
    return self._call_api('GET', ('dl', dt, address.zip, address.city, address.addr))

  def get_delivery_check(self, restaurant_id, date_time, address):
    """Call the dc API function with the given arguments."""
    dt = normalize(date_time, 'datetime')
    restaurant_id = normalize(restaurant_id, 'number')
    return self._call_api('GET', ('dc', restaurant_id, dt, address.zip, address.city, address.addr))

  def get_fee(self, restaurant_id, subtotal, tip, date_time, address):
    """Call the fee API function with the given arguments."""
    dt = normalize(date_time, 'datetime')
    restaurant_id = normalize(restaurant_id, 'number')
    subtotal = normalize(subtotal, 'money')
    tip = normalize(tip, 'money')
    return self._call_api('GET', ('fee', restaurant_id, subtotal, tip, dt, address.zip, address.city, address.addr))

  def get_details(self, restaurant_id):
    """Call the rd API function with the given id."""
    restaurant_id = normalize(restaurant_id, 'number')
    return self._call_api('GET', ('rd', restaurant_id))
