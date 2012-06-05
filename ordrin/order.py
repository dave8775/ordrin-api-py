from ordrinapi import OrdrinAPI

class Order(OrdrinAPI):

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    OrdrinAPI.__init__(self, url)

  def order(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, credit_card, login=None):
    data = {'restaurant_id':restaurant_id, 'tray':str(tray), 'tip':tip}
    data['delivery_date'] = _get_asap_or_date(delivery_date_time)
    if data['delivery_date'] != 'ASAP':
      data['delivery_time'] = delivery_date_time.strftime('%H:%M')
    data['first_name'] = first_name
    data['last_name'] = last_name
    data.update(address.make_dict())
    data['em'] = email
    data.update(credit_card.make_dict())
    return _call_api('POST', ('o', restaurant_id), login=login, data=data)

  def order_create_user(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, password, credit_card):
    data = {'restaurant_id':restaurant_id, 'tray':str(tray), 'tip':tip}
    data['delivery_date'] = _get_asap_or_date(delivery_date_time)
    if data['delivery_date'] != 'ASAP':
      data['delivery_time'] = delivery_date_time.strftime('%H:%M')
    data['first_name'] = first_name
    data['last_name'] = last_name
    data.update(address.make_dict())
    data['em'] = email
    data['password'] = Login.encrypt_password(password)
    data.update(credit_card.make_dict())
    return _call_api('POST', ('o', restaurant_id), login=login, data=data)
    
    
