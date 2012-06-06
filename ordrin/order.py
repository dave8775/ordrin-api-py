from ordrinapi import OrdrinAPI
from normalize import normalize

class OrderAPI(OrdrinAPI):

  def _build_dict(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, credit_card):
    data = {'restaurant_id':restaurant_id, 'tray':str(tray), 'tip':tip}
    data['delivery_date'] = self._get_asap_or_date(delivery_date_time)
    if data['delivery_date'] != 'ASAP':
      data['delivery_time'] = delivery_date_time.strftime('%H:%M')
    data['first_name'] = normalize(first_name, 'name')
    data['last_name'] = normalize(last_name, 'name')
    data.update(address.make_dict())
    data['em'] = normalize(email, 'email')
    data.update(credit_card.make_dict())
    return data

  def order(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, credit_card, login=None):
    
    data = _build_data(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, email, address, credit_card)
    return _call_api('POST', ('o', restaurant_id), login=login, data=data)

  def order_create_user(self, restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, password, credit_card):
    data = _build_data(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, email, address, credit_card)
    data['password'] = UserLogin.hash_password(password)
    return _call_api('POST', ('o', restaurant_id), login=login, data=data)
    
    
