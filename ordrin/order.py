from ordrinapi import OrdrinApi
from normalize import normalize
from data import UserLogin

class OrderApi(OrdrinApi):

  def _build_dict(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email, login=None):
    data = {'restaurant_id':restaurant_id, 'tray':str(tray), 'tip':tip}
    data['delivery_date'] = normalize(delivery_date_time, 'date')
    if data['delivery_date'] != 'ASAP':
      data['delivery_time'] = normalize(delivery_date_time, 'time')
    data['first_name'] = normalize(first_name, 'name')
    data['last_name'] = normalize(last_name, 'name')
    try:
      data.update(address.make_dict())
    except AttributeError:
      data['nick'] = normalize(address, 'nick')
    if not login:
      data['em'] = normalize(email, 'email')
    try:
      data.update({"card_"+k:v for k,v in credit_card.make_dict().iteritems()})
    except AttributeError:
      data['card_nick'] = normalize(credit_card, 'nick')
    data['type'] = 'res'
    return data

  def order(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email=None, login=None):
    data = self._build_dict(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email, login)
    return self._call_api('POST', ('o', restaurant_id), login=login, data=data)

  def order_create_user(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email, password):
    data = self._build_dict(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email)
    data['pw'] = UserLogin.hash_password(password)
    return self._call_api('POST', ('o', restaurant_id), data=data)
    
    
