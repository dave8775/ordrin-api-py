"""This package is a python wrapper for the ordr.in API."""
import restaurant, user, order

class APIs(object):

  def __init__(self, api_key, restaurant_url=None, user_url=None, order_url=None):
    """Sets up this module to make API calls. The first argument is the developer's
    API key. The other three are the urls corresponding to the three parts of the api.
    No API calls will work until this function is called"""
    if restaurant_url:
      self.restaurant = restaurant.RestaurantAPI(api_key, restaurant_url)
    if user_url:
      self.user = user.UserAPI(api_key, user_url)
    if order_url:
      self.order = order.OrderAPI(api_key, order_url)
