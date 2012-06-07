import datetime
import uuid
from pprint import pprint
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import ordrin
import ordrin.data

#
# Helper Decorator
#
def print_docstring_header(f):
  def g(*args, **kwargs):
    print ''
    print f.__doc__
    raw_input('Press enter to show')
    return f(*args, **kwargs)
  return g

#
# Global Variables
#
test_urls = {'restaurant_url': 'https://r-test.ordr.in/',
             'user_url': 'https://u-test.ordr.in/',
             'order_url': 'https://o-test.ordr.in/'}
api_key = raw_input("Please input your API key: ")

api = ordrin.APIs(api_key, **test_urls) #Create an API object
address = ordrin.data.Address('1 Main Street', 'College Station', 'TX', '77840', '(555) 555-5555')
credit_card = ordrin.data.CreditCard('Test User', '01', str(datetime.date.today().year+2), address, '4111111111111111', '123')
email = 'demo+{}@ordr.in'.format(uuid.uuid1().hex)
password = 'password'
login = ordrin.data.UserLogin(email, password)

#
# Restaurant demo functions
#
@print_docstring_header
def delivery_list_immediate_demo():
  """Get a list of restaurants that will deliver if you order now"""
  delivery_list_immediate = api.restaurant.get_delivery_list('ASAP', address)
  pprint(delivery_list_immediate, indent=4, depth=2)
  return delivery_list_immediate

@print_docstring_header
def delivery_list_future_demo():
  """Get a list of restaurants that will deliver if you order for 12 hours from now"""
  future_datetime = datetime.datetime.now()+datetime.timedelta(hours=12) #A timestamp twelve hours in the future
  delivery_list_later = api.restaurant.get_delivery_list(future_datetime, address)
  pprint(delivery_list_later, indent=4, depth=2)

@print_docstring_header
def delivery_check_demo(restaurant_id):
  """Get whether a particular restaurant will deliver if you order now"""
  delivery_check = api.restaurant.get_delivery_check(restaurant_id, 'ASAP', address)
  pprint(delivery_check, indent=4, depth=2)

@print_docstring_header
def fee_demo(restaurant_id):
  """Get fee and other info for ordering a given amount with a given tip"""
  subtotal = "$30.00"
  tip = "$5.00"
  fee_info = api.restaurant.get_fee(restaurant_id, subtotal, tip, 'ASAP', address)
  pprint(fee_info, indent=4, depth=2)

@print_docstring_header
def detail_demo(restaurant_id):
  """Get detailed information about a single restaurant"""
  restaurant_detail = api.restaurant.get_details(restaurant_id)
  pprint(restaurant_detail, indent=4, depth=3)

#
# Order demo functions
#
@print_docstring_header
def anonymous_order_demo(restaurant_id, tray):
  """Order food as someone without a user account"""
  tip = '$3.00'
  response = api.order.order(restaurant_id, tray, tip, 'ASAP', 'Test', 'User', address, credit_card, email)
  pprint(response)

#
# Main
#
delivery_list = delivery_list_immediate_demo()
delivery_list_future_demo()
restaurant_id = delivery_list[0]['id']
delivery_check_demo(restaurant_id)
fee_demo(restaurant_id)
detail_demo(restaurant_id)
