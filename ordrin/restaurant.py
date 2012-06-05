from ordrin import OrdrinAPI

class RestaurantAPI(OrdrinAPI):
  """This class will be used to access the restaurant API"""

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    OrdrinAPI.__init__(self, url)

  def get_delivery_list(date_time, address):
    """Calls the dl API function with the given arguments."""
    dt = self._get_asap_or_datetime(date_time)
    return self._call_api('GET', ('dl', dt, address.zip, address.city, address.addr))

  def get_delivery_check(restaurant_id, date_time, address):
    """Calls the dc API function with the given arguments."""
    dt = self._get_asap_or_datetime(date_time)
    return self._call_api('GET', ('dc', restaurant_id, dt, address.zip, address.city, address.addr))

  def get_fee(restaurant_id, subtotal, tip, date_time, address):
    """Calls the fee API function with the given arguments."""
    dt = self._get_asap_or_datetime(date_time)
    return self._call_api('GET', ('fee', subtotal, tip, dt, address.zip, address.city, address.addr))

  def get_details(restaurant_id):
    """Calls the rd API function with the given id."""
    return self._call_api('GET', ('rd', restaurant_id))
