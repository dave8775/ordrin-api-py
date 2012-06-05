"""This module contains classes for accessing the Ordr.in APIs. All method calls
return the same thing that the API calls do, but with JSON lists turned into Python
lists and JSON hashes turned into Python dicts. All arguments that call for a
datetime should be passed as a datetime.datetime object."""
import restaurant, user, order

class Ordrin(object):

  def __init__(self, api_key, restaurant_url=None, user_url=None, order_url=None):
    """Sets up this module to make API calls. The first argument is the developer's
    API key. The other three are the urls corresponding to the three parts of the api.
    No API calls will work until this function is called"""
    if restaurant_url:
      self.restaurant = restaurant.RestaurantAPI(api_key, restaurant_url)
    if user_url:
      self.user = user.UserAPI(api_key, user_url)
    if order_url:
      self.order = order.Order(api_key, order_url)
